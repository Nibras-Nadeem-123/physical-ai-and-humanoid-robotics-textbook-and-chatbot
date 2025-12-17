from typing import List, Dict

# Assuming the output of markdown_parser is plain text
def semantic_chunk_text(text: str, source_ref: str, min_chunk_size: int = 100) -> List[Dict]:
    """
    Breaks down plain text into semantically meaningful chunks.
    A simple approach: split by paragraphs and ensure minimum size.
    """
    chunks = []
    paragraphs = text.split('\n\n') # Split by double newlines for paragraphs

    current_chunk_text = ""
    for paragraph in paragraphs:
        stripped_paragraph = paragraph.strip()
        if not stripped_paragraph:
            continue

        if len(current_chunk_text) + len(stripped_paragraph) >= min_chunk_size:
            if current_chunk_text: # Add current chunk if it's not empty
                chunks.append({
                    "content": current_chunk_text.strip(),
                    "source_ref": source_ref # Add the source reference to the chunk
                })
            current_chunk_text = stripped_paragraph + "\n\n"
        else:
            current_chunk_text += stripped_paragraph + "\n\n"
    
    # Add any remaining text as a chunk
    if current_chunk_text:
        chunks.append({
            "content": current_chunk_text.strip(),
            "source_ref": source_ref
        })

    # Further refinement: ensure all chunks meet minimum size, merge if necessary
    final_chunks = []
    buffer_chunk = ""
    for chunk in chunks:
        buffer_chunk += chunk["content"] + "\n\n"
        if len(buffer_chunk) >= min_chunk_size:
            final_chunks.append({
                "content": buffer_chunk.strip(),
                "source_ref": chunk["source_ref"] # Use the source_ref of the last component
            })
            buffer_chunk = ""
    if buffer_chunk: # Add any leftover buffer
        final_chunks.append({
            "content": buffer_chunk.strip(),
            "source_ref": chunks[-1]["source_ref"] if chunks else source_ref
        })

    return final_chunks
