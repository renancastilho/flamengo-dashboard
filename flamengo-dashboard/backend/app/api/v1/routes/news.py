from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from typing import Optional, List

from app.core.database import get_db
from app.models.models import NewsArticle, SportCategory
from app.schemas.schemas import NewsArticleOut, NewsArticleCreate

router = APIRouter()


@router.get("/", response_model=List[NewsArticleOut])
async def list_news(
    sport: Optional[SportCategory] = Query(None, description="Filtrar por esporte"),
    featured: Optional[bool] = Query(None),
    limit: int = Query(20, le=100),
    offset: int = Query(0),
    db: AsyncSession = Depends(get_db),
):
    query = select(NewsArticle).order_by(desc(NewsArticle.published_at))
    if sport:
        query = query.where(NewsArticle.sport == sport)
    if featured is not None:
        query = query.where(NewsArticle.is_featured == featured)
    query = query.limit(limit).offset(offset)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/{news_id}", response_model=NewsArticleOut)
async def get_news(news_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(NewsArticle).where(NewsArticle.id == news_id))
    article = result.scalar_one_or_none()
    if not article:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    return article


@router.post("/", response_model=NewsArticleOut, status_code=201)
async def create_news(data: NewsArticleCreate, db: AsyncSession = Depends(get_db)):
    article = NewsArticle(**data.model_dump())
    db.add(article)
    await db.commit()
    await db.refresh(article)
    return article


@router.delete("/{news_id}", status_code=204)
async def delete_news(news_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(NewsArticle).where(NewsArticle.id == news_id))
    article = result.scalar_one_or_none()
    if not article:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    await db.delete(article)
    await db.commit()
