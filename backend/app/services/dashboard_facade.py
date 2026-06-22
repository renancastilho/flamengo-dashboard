from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import SportCategory, NewsArticle, Match
from app.schemas.schemas import NewsArticleCreate
from app.repositories.news_repository import NewsRepository
from app.repositories.match_repository import MatchRepository
from app.services.news_service import NewsService
from app.services.match_service import MatchService
from app.services.ai_service import AIService

# ==============================================================================
# FACADE PATTERN:
# Esse é o nosso "fachada" — ele simplifica o acesso a todos os serviços em um único lugar!
# Você não precisa mais se preocupar com repositórios, serviços separados — só usar esse Facade!
# ==============================================================================
class DashboardFacade:
    def __init__(self, db: AsyncSession):
        self.db = db
        
        # Aqui inicializamos tudo o que precisamos (repositórios e serviços)
        self.news_repo = NewsRepository(db)
        self.match_repo = MatchRepository(db)
        
        self.news_service = NewsService(self.news_repo)
        self.match_service = MatchService(self.match_repo)
        self.ai_service = AIService()

    # ------------------------------
    # Métodos para NOTÍCIAS
    # ------------------------------
    async def get_all_news(
        self,
        sport: Optional[SportCategory] = None,
        featured: Optional[bool] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[NewsArticle]:
        """Busca todas as notícias (com filtros opcionais)"""
        return await self.news_service.get_news_list(sport, featured, limit, offset)

    async def get_single_news(self, news_id: int) -> Optional[NewsArticle]:
        """Busca uma única notícia pelo ID"""
        return await self.news_service.get_article(news_id)

    async def create_new_news(self, data: NewsArticleCreate) -> NewsArticle:
        """Cria uma nova notícia"""
        return await self.news_service.create_article(data)

    async def remove_news(self, news_id: int) -> bool:
        """Remove uma notícia pelo ID (retorna True se deu certo)"""
        return await self.news_service.delete_article(news_id)

    # ------------------------------
    # Métodos para PARTIDAS
    # ------------------------------
    async def get_all_matches(
        self,
        sport: Optional[SportCategory] = None,
        completed: Optional[bool] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[Match]:
        """Busca todas as partidas (com filtros opcionais)"""
        return await self.match_service.get_matches_list(sport, completed, limit, offset)

    async def get_upcoming_games(self, limit: int = 10) -> List[Match]:
        """Busca os próximos jogos"""
        return await self.match_service.get_upcoming_matches(limit)

    # ------------------------------
    # Métodos para IA
    # ------------------------------
    async def ask_ai_question(self, question: str, context: Optional[str] = None):
        """Pergunta algo à IA especializada no Flamengo"""
        return await self.ai_service.get_chat_response(question, context)

    async def get_sport_ai_summary(self, sport: str):
        """Pede um resumo do desempenho do Flamengo em um esporte"""
        return await self.ai_service.get_sport_summary(sport)
