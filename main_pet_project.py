from fastapi import FastAPI

from contextlib import asynccontextmanager  # импортируем декоратор, который создает контекстные менеджеры

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова")
    yield
    print("Вылючение")


# приложение для планирования задач сотрудникам
app = FastAPI(lifespan=lifespan)

# подключим роуты
app.include_router(tasks_router)
