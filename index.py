import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from config import config

app = FastAPI(
    title="API for notepadvn v1",
    description="API for notepadvn v1",
    version="0.0.1"
)
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes import api

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=config.settings.port, log_level="info",reload=True)
    