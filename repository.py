from database import new_session, TaskOrm
from schemas import STaskAdd, STask
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()  # функция, превращает обьект к виду словарика
            task = TaskOrm(**task_dict)  # поля передаются через раскрытый словарь, как ключи
            session.add(task)  # добавляем обькт в сессию
            await session.flush()  # взять id для нашей таки
            await session.commit()  # отправляем изменения в базу данных
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:  # открываем сессию
            query = select(TaskOrm)  # получить все обьекты , обращаемсЯ к таблице
            result = await session.execute(query)  # обратись к базе даных через сесию и исполни этот query -итератор
            task_models = result.scalars().all()  # получить все обьекты итератора
            task_schemas = [
                STask.model_validate(task_model) for task_model in task_models
            ]  # конвертируем обьекты базы данных к пайд.схемам
            return task_schemas
