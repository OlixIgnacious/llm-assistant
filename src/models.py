import os
from typing import Optional
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def call_completion(prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 512, temperature: float = 0.0) -> str:
    resp = client.chat.completions.create(model = model, 
    messages = [{"role" : "system", "content": "You are a AnalystGPT"}, 
                {"role" : "user", "content": prompt}],
    max_tokens = max_tokens,
    temperature = temperature)
    return resp.choices[0].message.content