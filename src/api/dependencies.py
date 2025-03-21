from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

# для иньекции зависимости
SessionDep = Annotated[AsyncSession, Depends(get_session)]  # это и будем использовать потом в роуте
