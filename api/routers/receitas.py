from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.ReceitaSchema import ReceitaCreate, ReceitaResponse
from api.repositories.ReceitaRepository import (
    create_receita,
    get_all_receitas,
    update_receita,
    delete_receita,
)
from api.database import get_db  # função async para obter sessão

router = APIRouter(prefix="/receitas", tags=["Receitas"])

@router.get("/", response_model=list[ReceitaResponse])
async def listar_receitas(db: AsyncSession = Depends(get_db)):
    return await get_all_receitas(db)

@router.post("/", response_model=ReceitaResponse)
async def criar_receita(receita: ReceitaCreate, db: AsyncSession = Depends(get_db)):
    return await create_receita(receita, db)

@router.put("/{receita_id}", response_model=ReceitaResponse)
async def atualizar_receita(receita_id: int, receita: ReceitaCreate, db: AsyncSession = Depends(get_db)):
    receita_atualizada = await update_receita(receita_id, receita, db)
    if not receita_atualizada:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return receita_atualizada

@router.delete("/{receita_id}")
async def deletar_receita(receita_id: int, db: AsyncSession = Depends(get_db)):
    resultado = await delete_receita(receita_id, db)
    if resultado.get("message") == "Receita not found":
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return resultado
