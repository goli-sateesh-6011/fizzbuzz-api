from fastapi import FastAPI

from app.api import router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.get("/")
def root():
    return {
        "message": "FizzBuzz API is running!"
    }

app.include_router(router)

