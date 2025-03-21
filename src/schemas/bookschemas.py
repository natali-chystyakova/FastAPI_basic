from pydantic import BaseModel


class BookAddSchema(BaseModel):  # схема для пайдентик (без id, он генерируется сам)
    title: str
    author: str


class BookSchema(BookAddSchema):  # начледуется от первой схемы и добавляется id
    id: int
