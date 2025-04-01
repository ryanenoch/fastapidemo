from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Congrats! This is your first API!"}
