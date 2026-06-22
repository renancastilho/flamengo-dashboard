from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Optional, List
from app.api.v1.deps import get_dashboard_facade
from app.services.dashboard_facade import DashboardFacade
from app.models.models import SportCategory
from app.schemas.schemas import MatchOut

router = APIRouter()


@router.get("/", response_model=List[MatchOut])
async def list_matches(
    sport: Optional[SportCategory] = Query(None),
    completed: Optional[bool] = Query(None),
    limit: int = Query(10, le=50),
    facade: DashboardFacade = Depends(get_dashboard_facade),
):
    matches = await facade.get_all_matches(sport, completed, limit)
    return [MatchOut.from_orm_with_result(m) for m in matches]


@router.get("/upcoming", response_model=List[MatchOut])
async def upcoming_matches(
    limit: int = Query(5, le=20),
    facade: DashboardFacade = Depends(get_dashboard_facade),
):
    return await facade.get_upcoming_games(limit)


@router.get("/{match_id}", response_model=MatchOut)
async def get_match(
    match_id: int,
    facade: DashboardFacade = Depends(get_dashboard_facade),
):
    match = await facade.match_service.repository.get(match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Partida não encontrada")
    return MatchOut.from_orm_with_result(match)
