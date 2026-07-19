# All the endpoints are placed in this api.py file
from fastapi import APIRouter, Query
from typing import Annotated
from app.service import generate_fizzbuzz
from app.logger import logger
from app.config import settings
from app.statistics import record_request,get_most_frequent

router = APIRouter()

@router.get("/fizzbuzz")
def fizzbuzz(
    int1: Annotated[int, Query(gt=0)],
    int2: Annotated[int, Query(gt=0)],
    limit: Annotated[int, Query(gt=0)],
    str1: Annotated[str, Query(min_length=1)],
    str2: Annotated[str, Query(min_length=1)],
):
    logger.info(
        "FizzBuzz request: int1=%s int2=%s limit=%s str1=%s str2=%s",
        int1,
        int2,
        limit,
        str1,
        str2,
    )
    record_request(
        int1=int1,
        int2=int2,
        limit=limit,
        str1=str1,
        str2=str2,
    )

    return generate_fizzbuzz(
        int1=int1,
        int2=int2,
        limit=limit,
        str1=str1,
        str2=str2,
    )

@router.get("/health", tags=["Health"])
def health():
    logger.info("Health check requested")
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }

@router.get("/statistics", tags=["Statistics"])
def statistics():
    stats = get_most_frequent()

    if stats is None:
        return {
            "message": "No requests have been recorded yet."
        }
    
    return stats