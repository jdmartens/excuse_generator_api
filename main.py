from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an excuse generator. Provide a brief, creative, and plausible excuse."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"excuse": response.choices[0].message['content'].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

