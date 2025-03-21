# from fastapi import FastAPI, Depends
# from pydantic import BaseModel
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import select
# from typing import Annotated
#
# app=FastAPI()
#
# engine = create_async_engine("sqlite+aiosqlite:///books.db")
#
# #создаем сессию
# new_session = async_sessionmaker(engine, expire_on_commit=False)
#
# async def get_session():
#     async with new_session() as session:
#         yield session
#
# SessionDep= Annotated[AsyncSession, Depends(get_session)]
#
# class Base(DeclarativeBase):
#     pass
#
# class BookModel(Base):
#     __tablename__:str="books"
#     id:Mapped[int] = mapped_column(primary_key=True)
#     title:Mapped[str]
#     author:Mapped[str]
#
# @app.post("/setup_database")
# async def setup_database():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     return {"OK":True}
#
# class BookAddSchema(BaseModel):
#     title: str
#     author: str
#
# class BookSchema(BookAddSchema):
#     id: int
#
#
# @app.post("/books")
# async def add_book(data: BookAddSchema, session: SessionDep):
#     new_book = BookModel(
#         title =data.title,
#         author = data.author,
#     )
#     session.add(new_book)  # в сессию добавили новый обьект
#     await session.commit()  # закомитить изменения в базу данных
#     return {"ok": True}
#
# @app.get("/books")
# async def get_books(session: SessionDep):
#     query = select(BookModel)
#     result = await session.execute(query) # тут вернется итератор
#     return result.scalars().all()  # вернем все книжки


# повторение


from fastapi import FastAPI
from src.api import main_router


app = FastAPI()  # создаем обьект фастапи
app.include_router(main_router)  # добавим роутеры из src.api в главный файл
