from fastapi import FastAPI
import os

app = FastAPI()

FILE = "memory.txt"


def load_messages():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return f.readlines()


def save_messages(messages):
    with open(FILE, "w") as f:
        f.writelines(messages)


@app.post("/send")
def send_message(message: str):
    messages = load_messages()
    messages.append("\n")
    messages.append(message)
    save_messages(messages)
    return {"message": "Message received"}


@app.get("/messages")
def get_messages():
    return {"messages": load_messages()}


@app.get("/clear")
def clear_messages(password: str):
    if password != "sihua":
        return {"message": "Unauthorized"}
    save_messages([])
    return {"message": "Messages cleared"}
