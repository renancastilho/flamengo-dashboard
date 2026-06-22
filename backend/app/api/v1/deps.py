from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.dashboard_facade import DashboardFacade

async def get_dashboard_facade(
    db: AsyncSession = Depends(get_db)
) -> DashboardFacade:
    return DashboardFacade(db)
