from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.database import create_tables  # Função async para criar tabelas
from api.routers import receitas

app = FastAPI(
    title="Receitas API",
    description="API para gerenciamento de receitas",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(receitas.router)

@app.on_event("startup")
async def on_startup():
    await create_tables()  # cria as tabelas na inicialização

@app.get("/")
async def root():
    return {"message": "API Receitas está online!"}
