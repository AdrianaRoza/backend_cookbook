from api.models.ReceitaModel import Receita
from api.schemas.ReceitaSchema import ReceitaCreate
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

# C CREATE
async def create_receita(request_body: ReceitaCreate, db: AsyncSession):
    ingredientes = (
        ", ".join(request_body.ingredients)
        if isinstance(request_body.ingredients, list)
        else request_body.ingredients
    )

    preparation = (
        ", ".join(request_body.preparation)
        if isinstance(request_body.preparation, list)
        else request_body.preparation
    )

    nova_receita = Receita(
        title=request_body.title,
        description=request_body.description,
        author=request_body.author,
        date=request_body.date,
        time=request_body.time,
        ingredients=ingredientes,
        preparation=preparation,
        category=request_body.category,
        is_active=True
    )
    db.add(nova_receita)
    await db.commit()
    await db.refresh(nova_receita)
    return nova_receita

# R READ
async def get_all_receitas(db: AsyncSession):
    query = select(Receita)
    result = await db.execute(query)
    return result.scalars().all()

# U UPDATE
async def update_receita(receita_id: int, request_body: ReceitaCreate, db: AsyncSession):
    receita = await db.get(Receita, receita_id)
    if not receita:
        return {"message": "Receita not found"}

    ingredientes = (
        ", ".join(request_body.ingredients)
        if isinstance(request_body.ingredients, list)
        else request_body.ingredients
    )

    preparation = (
        ", ".join(request_body.preparation)
        if isinstance(request_body.preparation, list)
        else request_body.preparation
    )

    receita.title = request_body.title
    receita.description = request_body.description
    receita.author = request_body.author
    receita.date = request_body.date
    receita.time = request_body.time
    receita.ingredients = ingredientes
    receita.preparation = preparation
    receita.category = request_body.category 

    await db.commit()
    await db.refresh(receita)
    return receita

# D DELETE
async def delete_receita(receita_id: int, db: AsyncSession):
    receita = await db.get(Receita, receita_id)
    if not receita:
        return {"message": "Receita not found"}

    await db.delete(receita)
    await db.commit()
    return {"message": "Receita deleted successfully"}
