from fastapi import FastAPI
import os

app = FastAPI()
SERVICE_NAME = os.getenv("SERVICE_NAME", "orders")
INSTANCE_ID = os.getenv("INSTANCE_ID", "1")


@app.get("/")
async def root():
    return {"service": SERVICE_NAME, "instance": INSTANCE_ID, "status": "running"}


@app.get("/orders")
async def get_orders():
    return {
        "service": "orders",
        "data": [
            {
            "id": 1,
            "item": "Item A",
            "price": 10.0
            },
            {
            "id": 2,
            "item": "Item B",
            "price": 20.0
            }
        ],
    }
