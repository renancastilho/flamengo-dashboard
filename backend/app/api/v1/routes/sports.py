from fastapi import APIRouter
from app.models.models import SportCategory

router = APIRouter()

SPORTS_DATA = {
    SportCategory.FUTEBOL: {
        "name": "Futebol",
        "icon": "ball-football",
        "competitions": ["Brasileirão Série A", "Copa do Brasil", "Libertadores", "Supercopa"],
        "founded_year": 1911,
        "titles_count": 43,
        "current_position": {"competition": "Brasileirão 2025", "position": 1, "points": 42},
    },
    SportCategory.BASQUETE: {
        "name": "Basquete",
        "icon": "ball-basketball",
        "competitions": ["NBB", "Champions League Americas"],
        "founded_year": 2008,
        "titles_count": 3,
        "current_position": {"competition": "NBB 2025", "position": 2, "points": None},
    },
    SportCategory.NATACAO: {
        "name": "Natação",
        "icon": "wave-sine",
        "competitions": ["Troféu Brasil", "Maria Lenk", "Pan-Americano"],
        "founded_year": 1895,
        "titles_count": 120,
        "current_position": None,
    },
    SportCategory.VOLEI: {
        "name": "Vôlei",
        "icon": "ball-volleyball",
        "competitions": ["Superliga Masculina"],
        "founded_year": 2023,
        "titles_count": 0,
        "current_position": None,
    },
    SportCategory.REMO: {
        "name": "Remo",
        "icon": "rowing",
        "competitions": ["Brasileiro de Remo", "Pan-Americano"],
        "founded_year": 1895,
        "titles_count": 50,
        "current_position": None,
    },
    SportCategory.ESPORTS: {
        "name": "eSports",
        "icon": "device-gamepad-2",
        "competitions": ["CBLOL", "Rainbow Six", "VALORANT"],
        "founded_year": 2019,
        "titles_count": 2,
        "current_position": {"competition": "CBLOL 2025", "position": 3, "points": None},
    },
}


@router.get("/")
async def list_sports():
    return [{"category": k.value, **v} for k, v in SPORTS_DATA.items()]


@router.get("/{sport_category}")
async def get_sport(sport_category: SportCategory):
    data = SPORTS_DATA.get(sport_category)
    if not data:
        return {"error": "Esporte não encontrado"}
    return {"category": sport_category.value, **data}
