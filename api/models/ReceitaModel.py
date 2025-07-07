from sqlalchemy import JSON, Column, Integer, String, Boolean, Date, Time
from api.database import Base

class Receita(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    author = Column(String)
    date = Column(Date)
    time = Column(Time)
    ingredients = Column(String)  # ou JSON, se quiser lista
    is_active = Column(Boolean, default=True)
