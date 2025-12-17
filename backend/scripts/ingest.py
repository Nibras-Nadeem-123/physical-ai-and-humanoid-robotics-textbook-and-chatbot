import argparse
import os
from uuid import uuid4

from qdrant_client import QdrantClient, models

from backend.src.app.core.config import settings
from backend.src.data_ingestion.markdown_parser import parse_markdown
from backend.src.data_ingestion.chunking import chunk_text

import openai
from typing import List

# Embedding client
class EmbeddingClient:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        response = openai.Embedding.create(
            input=texts,
            model="text-embedding-ada-002"
        )
        return [item['embedding'] for item in response['data']]

# Initialize Qdrant client
qdrant_client = QdrantClient(host=settings.QDRANT_HOST, api_key=settings.QDRANT_API_KEY)

# Initialize Embedding client
embedding_client = EmbeddingClient(api_key=settings.OPENAI_API_KEY)

COLLECTION_NAME = "textbook_chunks"

def create_qdrant_collection():
    print(f"Creating Qdrant collection: {COLLECTION_NAME}")
    qdrant_client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=1536, distance=models.Distance.COSINE),
    )

def ingest_data(input_dir: str):
    create_qdrant_collection()
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".md") or filename.endswith(".mdx"):
            filepath = os.path.join(input_dir, filename)
            print(f"Processing {filepath}...")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            plain_text = parse_markdown(markdown_content)
            
            # Use filename as a simplified source reference for now
            source_ref = os.path.splitext(filename)[0]
            chunk_strings = chunk_text(plain_text)
            
            chunks = [{"content": text, "source_ref": f"{source_ref}-p{i+1}"} for i, text in enumerate(chunk_strings)]
            
            # Get embeddings for all chunk contents
            chunk_contents = [chunk["content"] for chunk in chunks]
            embeddings = embedding_client.get_embeddings(chunk_contents)
            
            points = []
            for i, chunk in enumerate(chunks):
                points.append(
                    models.PointStruct(
                        id=str(uuid4()),
                        vector=embeddings[i],
                        payload={
                            "content": chunk["content"], 
                            "source_ref": chunk["source_ref"],
                            "document_id": filename
                        },
                    )
                )
            
            print(f"Uploading {len(points)} points to Qdrant...")
            qdrant_client.upsert(
                collection_name=COLLECTION_NAME,
                wait=True,
                points=points
            )
            print(f"Finished processing {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Markdown textbook data into Qdrant.")
    parser.add_argument("--input-dir", type=str, required=True, help="Directory containing Markdown files.")
    
    args = parser.parse_args()
    
    ingest_data(args.input_dir)