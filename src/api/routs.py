from fastapi import APIRouter
from sqlalchemy import select
from src.api.dependencies import SessionDep
from src.database import engine, Base
from src.models.books import BookModel
from src.schemas.bookschemas import BookAddSchema


router = APIRouter()


# создадим функцию, которая будет записывать все в базу данных
@router.post("/setup_database")  # делаем путь (роут) для создания запуска функции и создания таблици
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"OK": True}


# Для создания записи в таблицу  делаем роут
@router.post("/books")
async def add_book(data: BookAddSchema, session: SessionDep):
    new_book = BookModel(
        title=data.title,
        author=data.author,
    )  # модель из орм с полями, значения берем из пайдентик схемы
    session.add(new_book)  # в сессию алхимии добавляем новый обьект
    await session.commit()  # заkомитить изменения в базу данных
    return {"OK": True}


# получение всех книг из базы данных
@router.get("/books")
async def get_book(session: SessionDep):
    query = select(BookModel)  # выбрать BookModel
    result = await session.execute(query)  # исполнить код в скобочках
    return result.scalars().all()  # вернуть все
