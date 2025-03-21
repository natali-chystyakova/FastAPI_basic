from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)  # импортируем создание асинхронного движка для работы с бд
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

import os

# Определяем путь к базе данных
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Получаем путь к текущей папке
DB_PATH = os.path.join(BASE_DIR, "db_data", "tasks.db")  # Создаём путь к базе

# Проверяем, есть ли папка db_data, если нет — создаём
if not os.path.exists(os.path.dirname(DB_PATH)):
    os.makedirs(os.path.dirname(DB_PATH))

# Создаём движок для подключения к SQLite
DATABASE_URL = f"sqlite+aiosqlite:///{DB_PATH}"
engine = create_async_engine(DATABASE_URL)


# engine = create_async_engine(
#     'sqlite+aiosqlite:///db_data/tasks.db'
#
# )

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"  # название таблици
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]


# создадим функцию, которая будет создавать таблицу
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


# удаление таблиц
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
