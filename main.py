from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from openai import OpenAI
import os

class Settings(BaseSettings):
    openai_api_key: str
    debug_mode: bool = False
    origins: str = "http://localhost:4200"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
app = FastAPI()

# Configure CORS
origins = settings.origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/homework-excuse", response_model=Excuse)
async def get_homework_excuse():
    return await generate_excuse("Generate an excuse for why you didn't finsish your homework")

@app.get("/chore-excuse", response_model=Excuse)
async def get_chore_excuse():
    return await generate_excuse("You are 12 years old and you need an excuse for why you didn't do your chores")

@app.get("/custom-excuse", response_model=Excuse)
async def get_custom_excuse(prompt: str = "Generate a custom excuse", system_role: str = "You are an excuse generator. Provide a brief, creative, and plausible excuse."):
    return await generate_excuse(prompt, system_role)

async def generate_excuse(prompt, system_role="You are an excuse generator. Provide a brief, creative, and plausible excuse."):
    prompt = prompt + ". Do not use a cat/feline excuse."
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": prompt}
        ])
        return {"excuse": response.choices[0].message.content.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
