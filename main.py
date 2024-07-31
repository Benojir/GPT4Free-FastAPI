from g4f.client import Client
import sys
import platform

from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/")
def read_prompt(prompt: str = Form(...)):
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
