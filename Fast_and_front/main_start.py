from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["http://localhost:63342"]  # * - все сайты в интернете могут к нам обращаться
)


@app.get("/", summary="Главный путь", tags=["Основные пути"])
def home():
    return "Hello World!!!"


books = [
    {
        "id": 1,
        "title": "Асинхронность в Python",
        "author": "Мэттью",
    },
    {
        "id": 2,
        "title": "Beckend разработка на Python",
        "author": "Артем",
    },
]


@app.get("/books", tags=["Книги 📚"], summary="Получить все книги")
def read_books():
    return books


@app.get("/books/{book_id}", tags=["Книги"], summary="Получить конкретную книги")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


class Newbook(BaseModel):
    title: str
    author: str


@app.post("/books", tags=["Книги"])
def create_book(new_book: Newbook):
    books.append(
        {
            "id": len(books) + 1,
            "title": new_book.title,
            "author": new_book.author,
        }
    )
    return {"success": True, "message": "Книга успешно добавлена"}


#
# if __name__=="__main__":
#     uvicorn.run("main:app", reload=True)

# if __name__=="__main__":
#     uvicorn.run("main_start:app", reload=True)
