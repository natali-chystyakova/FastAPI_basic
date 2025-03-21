from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskID

router = APIRouter(
    prefix="/tasks",  # поставить этим таскам одинаковый маршрут,который начинается с
    tags=["Таски"],  # поменять на странице слово default
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],  # тут мы принимаем нашу таску в формате pydantic схемы
) -> STaskID:
    # tasks.append(task) # добавляем эту таскув список
    task_id = await TaskRepository.add_one(task)

    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()  # асинхронный запрос к репозиторию, чтобы взять все таски
    # return {"data": tasks}
    return tasks


# uvicorn main_pet_project:app --reload
