from fastapi import APIRouter, Depends
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

from auth.base_config import active_user
from auth.models import User

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("/{item_id}")
async def get_operation(item_id: int, session: AsyncSession = Depends(get_async_session),user: User = Depends(active_user)):
    query = sa.select(operation).where(operation.c.id == item_id)
    res =  await session.execute(query)
    return res.all()

@router.get("/type/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = sa.select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = sa.insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}