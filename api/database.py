from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use o driver asyncpg na URL
DATABASE_URL = "postgresql+asyncpg://postgres:992690363note@localhost:5432/receitas_db"

Base = declarative_base()

# Cria a engine async — sem pool_size/max_overflow!
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Cria a fábrica de sessões async
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Função dependência para o FastAPI — cria uma sessão para cada request e fecha depois
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

# Função para criar as tabelas no banco (rodar em startup)
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
