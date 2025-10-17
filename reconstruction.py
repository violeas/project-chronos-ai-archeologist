import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("GEMINI_API_KEY")

def reconstruct_text(fragment):
    prompt = f"Reconstruct the following text, preserving style and filling in missing context:\n{fragment}"
    
    response = openai.ChatCompletion.create(
        model="gemini-1",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    
    reconstructed = response['choices'][0]['message']['content']
    return reconstructed
