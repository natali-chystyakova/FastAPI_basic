from fastapi import APIRouter

from src.api.routs import router as books_router

main_router = APIRouter()
main_router.include_router(books_router)
