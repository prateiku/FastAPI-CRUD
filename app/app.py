from fastapi import FastAPI

from routes import router

app = FastAPI()

app.include_router(router, tags=["Api"])


@app.get("/", tags=["Index"])
async def index():
    return {"message": "CRUD api implemented using FastAPI"}
