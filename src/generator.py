import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


# Load .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")


# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_answer(query, context):
    """
    Generate an answer using Gemini based only on the retrieved context.
    """

    prompt = f"""
You are a RAG assistant for the Almamlaka TV Digital Expansion Initiative.

Answer the user's question ONLY using the information provided
in the context below.

Rules:
- Do not use outside knowledge.
- Do not make assumptions.
- Do not invent information.
- If the answer is not available in the provided context, say:
  "The information is not available in the provided documents."
- If the user asks in Arabic, answer in Arabic.
- If the user asks in English, answer in English.
- If the user mixes Arabic and English, answer naturally using the dominant language.

Context:
{context}

User Question:
{query}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text