from pydantic import BaseModel
from datetime import date, time
from typing import Union

class ReceitaCreate(BaseModel):
    title: str
    description: str
    author: str
    date: date
    time: time
    ingredients: Union[str, list[str]]
    category: str

class ReceitaResponse(ReceitaCreate):
    id: int
    is_active: bool
    category:str

    class Config:
        from_attributes = True
