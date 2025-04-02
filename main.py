from fastapi import FastAPI
from gas import gas

app = FastAPI()
price = gas()

@app.get("/")
async def root():
    return {"Message": "Congrats! This is your first API!"}
    return price
