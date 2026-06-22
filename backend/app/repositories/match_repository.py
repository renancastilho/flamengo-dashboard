from typing import List, Optional
from sqlalchemy import select, desc
from app.repositories.base import BaseRepository
from app.models.models import Match, SportCategory

class MatchRepository(BaseRepository[Match]):
    def __init__(self, db):
        super().__init__(Match, db)

    async def list_matches(
        self,
        sport: Optional[SportCategory] = None,
        completed: Optional[bool] = None,
        limit: int = 20,
        offset: int = 0
    ) -> List[Match]:
        query = select(Match).order_by(desc(Match.match_date))
        if sport:
            query = query.where(Match.sport == sport)
        if completed is not None:
            query = query.where(Match.is_completed == completed)
        
        query = query.limit(limit).offset(offset)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_upcoming_matches(self, limit: int = 10) -> List[Match]:
        query = (
            select(Match)
            .where(Match.is_completed == False)
            .order_by(Match.match_date)
            .limit(limit)
        )
        result = await self.db.execute(query)
        return result.scalars().all()
