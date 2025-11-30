import os

from fastapi import FastAPI

app = FastAPI()
SERVICE_NAME = os.getenv("SERVICE_NAME", "users")
INSTANCE_ID = os.getenv("INSTANCE_ID", "1")


@app.get("/")
async def root():
    return {"service": SERVICE_NAME, "instance": INSTANCE_ID, "status": "running"}


@app.get("/users")
async def get_users():
    return {
        "service": "users",
        "data": [
            {
            "id": 1,
            "name": "User 1"
            },
            {
            "id": 2,
            "name": "User 2"
            }
        ],
    }
