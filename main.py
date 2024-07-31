from g4f.client import Client
import asyncio
from typing import Union

from fastapi import FastAPI

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

@app.get("/")
async def show_error():
    return {"error" : "Authentication required."}

@app.post("/promt/{user_promt}")
async def read_promt(user_promt: str):
    client = Client()
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": f"{user_promt}"}],
        )
        reply = response.choices[0].message.content
        return {"response" : reply}
    except:
        return {"error" : "Something wrong!"}

