from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class BookModel(Base):  # обьявили модель(таблицу) в ORM (в базе данных мы ее еще не создали)
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
