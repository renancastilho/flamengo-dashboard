from typing import List, Optional
from app.repositories.news_repository import NewsRepository
from app.models.models import SportCategory, NewsArticle
from app.schemas.schemas import NewsArticleCreate

class NewsService:
    def __init__(self, repository: NewsRepository):
        self.repository = repository

    async def get_news_list(
        self,
        sport: Optional[SportCategory] = None,
        featured: Optional[bool] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[NewsArticle]:
        return await self.repository.list_news(sport, featured, limit, offset)

    async def get_article(self, article_id: int) -> Optional[NewsArticle]:
        return await self.repository.get(article_id)

    async def create_article(self, data: NewsArticleCreate) -> NewsArticle:
        return await self.repository.create(data.model_dump())

    async def delete_article(self, article_id: int) -> bool:
        return await self.repository.delete(article_id)
