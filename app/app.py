from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()



@app.put("/ComUnity")
async def mandarDatos():
    return ""