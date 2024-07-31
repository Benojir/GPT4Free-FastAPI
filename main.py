from g4f.client import Client
import asyncio
import sys
import platform

from fastapi import FastAPI, Form

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

@app.post("/")
async def read_prompt(prompt: str = Form(...)):
    client = Client()
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"{prompt}"}],
        )
        reply = response.choices[0].message.content
        return {"response": reply}
    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}
