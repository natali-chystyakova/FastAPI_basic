# from fastapi import FastAPI, BackgroundTasks
# import time
# import asyncio
#
#
# app = FastAPI()
#
# def sync_task():
#     time.sleep(3)
#     print("Отправляем email")
#
# async def async_task():
#     await asyncio.sleep(3)
#     print("Сделан запрос в сторонний API")
#
#
# # @app.post("/")  # тут если функции асинхронные
# # async def some_route():
# #     ...
# #     #sync_task()
# #     #await async_task()
# #     asyncio.create_task(async_task()) # (помещаем в скобки корутину) так мы запускам фоново
# #     return {"ok": True}
#
# @app.post("/") # тут, если фукции синхронные
# async def some_route(background_tasks: BackgroundTasks):
#     ...
#     background_tasks.add_task(sync_task)# (помещаем в скобки синхронную и не вызываем) так мы запускам фоново
#     return {"ok": True}

# повторение
from fastapi import FastAPI, BackgroundTasks
import time
import asyncio

app = FastAPI()


def sync_task():
    time.sleep(3)
    print("Отправляем email")


async def async_task():
    await asyncio.sleep(3)
    print("Сделан запрос в стороннее API")


@app.post("/")
async def some_rout(background_tasks: BackgroundTasks):
    ...
    # await async_task() # точтно так же будем ждать
    # sync_task() # если запустить просто, как есть, будем ждать 3 секунды
    # asyncio.create_task(async_task()) # если функция асинхронная
    background_tasks.add_task(sync_task)  # если функция синхронная
    return {"ok": True}
