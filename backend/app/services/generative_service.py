import openai
from typing import List, Dict

from app.core.config import settings

class GenerativeService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY

    def generate_response(self, prompt: str, context: List[Dict]) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful assistant for a Physical AI & Humanoid Robotics textbook. Answer questions based on the provided context."},
            {"role": "user", "content": f"Context: 
{' '.join([c['content'] for c in context])}

Question: {prompt}"}
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # Or gpt-4, depending on availability and cost
            messages=messages,
            max_tokens=500
        )
        return response.choices[0].message['content']
