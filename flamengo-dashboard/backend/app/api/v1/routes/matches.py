from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from typing import Optional, List
from datetime import datetime

from app.core.database import get_db
from app.models.models import Match, SportCategory
from app.schemas.schemas import MatchOut

router = APIRouter()


@router.get("/", response_model=List[MatchOut])
async def list_matches(
    sport: Optional[SportCategory] = Query(None),
    completed: Optional[bool] = Query(None),
    limit: int = Query(10, le=50),
    db: AsyncSession = Depends(get_db),
):
    query = select(Match).order_by(desc(Match.match_date))
    if sport:
        query = query.where(Match.sport == sport)
    if completed is not None:
        query = query.where(Match.is_completed == completed)
    query = query.limit(limit)
    result = await db.execute(query)
    matches = result.scalars().all()
    return [MatchOut.from_orm_with_result(m) for m in matches]


@router.get("/upcoming", response_model=List[MatchOut])
async def upcoming_matches(
    sport: Optional[SportCategory] = Query(None),
    db: AsyncSession = Depends(get_db),
):
    now = datetime.utcnow()
    query = (
        select(Match)
        .where(Match.match_date >= now, Match.is_completed == False)
        .order_by(Match.match_date)
        .limit(5)
    )
    if sport:
        query = query.where(Match.sport == sport)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/{match_id}", response_model=MatchOut)
async def get_match(match_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Match).where(Match.id == match_id))
    match = result.scalar_one_or_none()
    if not match:
        raise HTTPException(status_code=404, detail="Partida não encontrada")
    return MatchOut.from_orm_with_result(match)
