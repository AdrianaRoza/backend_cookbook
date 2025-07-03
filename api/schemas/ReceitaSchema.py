from pydantic import BaseModel
from datetime import date, time
from typing import Union

class ReceitaCreate(BaseModel):
    title: str
    description: str
    author: str
    date: date
    time: time
    ingredients: Union[str, list[str]]  # <-- aceita string ou lista

class ReceitaResponse(ReceitaCreate):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # Pydantic v2
