from fastapi import FastAPI

app = FastAPI()

@app.get("/get-message")
async def root():
    return {"Message": "Congrats! This is your first API!"}
