
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_node():
    return {'Hello':'World'}