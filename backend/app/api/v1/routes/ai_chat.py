from fastapi import APIRouter, Depends, HTTPException
from app.schemas.schemas import AIChatRequest, AIChatResponse
from app.api.v1.deps import get_dashboard_facade
from app.services.dashboard_facade import DashboardFacade

router = APIRouter()


@router.post("/chat", response_model=AIChatResponse)
async def ai_chat(
    request: AIChatRequest,
    facade: DashboardFacade = Depends(get_dashboard_facade)
):
    try:
        return await facade.ask_ai_question(request.question, request.context)
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.get("/summary/{sport}")
async def sport_summary(
    sport: str,
    facade: DashboardFacade = Depends(get_dashboard_facade)
):
    try:
        return await facade.get_sport_ai_summary(sport)
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))
