from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from openai import OpenAI
import os

class Settings(BaseSettings):
    openai_api_key: str
    debug_mode: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
app = FastAPI()

client = OpenAI(api_key=settings.openai_api_key)

class Excuse(BaseModel):
    excuse: str

@app.get("/work-excuse", response_model=Excuse)
async def get_work_excuse():
    return await generate_excuse("Generate an excuse for why something is not done yet at work")

@app.get("/late-excuse", response_model=Excuse)
async def get_late_excuse():
    return await generate_excuse("Generate an excuse for why you were late")

@app.get("/help-excuse", response_model=Excuse)
async def get_help_excuse():
    return await generate_excuse("Generate an excuse for why you can't help someone")

@app.get("/busy-excuse", response_model=Excuse)
async def get_busy_excuse():
    return await generate_excuse("Generate an excuse for why you can't go to some event")

async def generate_excuse(prompt):
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an excuse generator. Provide a brief, creative, and plausible excuse."},
            {"role": "user", "content": prompt}
        ])
        return {"excuse": response.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

