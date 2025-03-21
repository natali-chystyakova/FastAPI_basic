# тестирование файла  main_start

import pytest
from httpx import AsyncClient, ASGITransport
from Fast_and_front.main_start import app  # импортируем приложение, которое app = FastAPI()

# def func(num: int):
#     return 1/num
#
# def test_func():
#     assert func(1)==1  #убедись, что вызов функции с 1 == 1
#     assert func(2)==0.5


@pytest.mark.asyncio  # если мы вызываем асинхронные тесты, то помечаем их декоатором
async def test_read_books():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        response = await ac.get("/books")
        assert response.status_code == 200  # удостоверимся, что статус 200

        data = response.json()
        # assert data==[] # удостоверимся,  что data - пустой список
        assert len(data) == 2  # убедимся. что у нас есть 2 книжки


# протестируем пост запрос
@pytest.mark.asyncio  # если мы вызываем асинхронные тесты, то помечаем их декоатором
async def test_create_book():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        response = await ac.post(
            "/books",
            json={
                "title": "Nazvanie",
                "author": "Author",
            },
        )
        assert response.status_code == 200  # удостоверимся, что статус 200

        data = response.json()
        # assert data==[] # удостоверимся,  что data - пустой список
        assert data == {"success": True, "message": "Книга успешно добавлена"}  # убедимся.  что эти данные вернулись
