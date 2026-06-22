from typing import List, Optional
from app.repositories.match_repository import MatchRepository
from app.models.models import SportCategory, Match
from app.schemas.schemas import MatchCreate

class MatchService:
    def __init__(self, repository: MatchRepository):
        self.repository = repository

    async def get_matches_list(
        self,
        sport: Optional[SportCategory] = None,
        completed: Optional[bool] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[Match]:
        return await self.repository.list_matches(sport, completed, limit, offset)

    async def get_upcoming_matches(self, limit: int = 10) -> List[Match]:
        return await self.repository.get_upcoming_matches(limit)

    async def create_match(self, data: MatchCreate) -> Match:
        return await self.repository.create(data.model_dump())
