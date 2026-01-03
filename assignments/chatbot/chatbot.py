from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
import os

router = APIRouter()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Request schema
class ChatRequest(BaseModel):
    message: str
    lang: str = "en"

# Language map
LANG_MAP = {
    "en": "Reply in English.",
    "te": "Reply in Telugu.",
    "hi": "Reply in Hindi.",
    "ta": "Reply in Tamil.",
    "kn": "Reply in Kannada.",
    "ml": "Reply in Malayalam."
}

@router.post("/chat")
async def chat(req: ChatRequest):
    system_prompt = (
        "You are an air quality assistant. "
        "Give short, clear answers about AQI, air pollution, and health effects."
    )

    lang_instruction = LANG_MAP.get(req.lang, "Reply in English.")

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=[
                {
                    "role": "system",
                    "content": system_prompt + " " + lang_instruction
                },
                {
                    "role": "user",
                    "content": req.message
                }
            ],
            max_output_tokens=100
        )

        return {"reply": response.output_text}

    except Exception as e:
        print("Chatbot error:", e)
        return {"reply": "AI service temporarily unavailable."}
