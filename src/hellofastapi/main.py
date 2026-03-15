# main.py
from fastapi import FastAPI
import socket
from pydantic import BaseModel

app = FastAPI()

class HostResponse(BaseModel):
    message: str
    hostname: str

@app.get("/hello", response_model=HostResponse)
async def get_hostname():
    return HostResponse(
    message="Hello there!",
    hostname=socket.gethostname()
)
