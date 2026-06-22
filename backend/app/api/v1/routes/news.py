from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Optional, List
from app.api.v1.deps import get_dashboard_facade
from app.services.dashboard_facade import DashboardFacade
from app.models.models import SportCategory
from app.schemas.schemas import NewsArticleOut, NewsArticleCreate

router = APIRouter()


@router.get("/", response_model=List[NewsArticleOut])
async def list_news(
    sport: Optional[SportCategory] = Query(None, description="Filtrar por esporte"),
    featured: Optional[bool] = Query(None),
    limit: int = Query(20, le=100),
    offset: int = Query(0),
    facade: DashboardFacade = Depends(get_dashboard_facade),
):
    return await facade.get_all_news(sport, featured, limit, offset)


@router.get("/{news_id}", response_model=NewsArticleOut)
async def get_news(
    news_id: int,
    facade: DashboardFacade = Depends(get_dashboard_facade),
):
    article = await facade.get_single_news(news_id)
    if not article:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    return article


@router.post("/", response_model=NewsArticleOut, status_code=201)
async def create_news(
    data: NewsArticleCreate,
    facade: DashboardFacade = Depends(get_dashboard_facade),
):
    return await facade.create_new_news(data)


@router.delete("/{news_id}", status_code=204)
async def delete_news(
    news_id: int,
    facade: DashboardFacade = Depends(get_dashboard_facade),
):
    success = await facade.remove_news(news_id)
    if not success:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
