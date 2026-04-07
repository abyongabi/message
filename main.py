from fastapi import FastAPI
import json
import os

app = FastAPI()

FILE = "memory.json"


def load_messages():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_messages(messages):
    with open(FILE, "w") as f:
        json.dump(messages, f)


@app.post("/send")
def send_message(message: str):
    messages = load_messages()
    messages.append(message)
    save_messages(messages)
    return {"message": "Message received"}


@app.get("/messages")
def get_messages():
    return {"messages": load_messages()}
