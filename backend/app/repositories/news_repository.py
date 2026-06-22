from typing import List, Optional
from sqlalchemy import select, desc
from app.repositories.base import BaseRepository
from app.models.models import NewsArticle, SportCategory

class NewsRepository(BaseRepository[NewsArticle]):
    def __init__(self, db):
        super().__init__(NewsArticle, db)

    async def list_news(
        self,
        sport: Optional[SportCategory] = None,
        featured: Optional[bool] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[NewsArticle]:
        query = select(NewsArticle).order_by(desc(NewsArticle.published_at))
        if sport:
            query = query.where(NewsArticle.sport == sport)
        if featured is not None:
            query = query.where(NewsArticle.is_featured == featured)
        
        query = query.limit(limit).offset(offset)
        result = await self.db.execute(query)
        return result.scalars().all()
