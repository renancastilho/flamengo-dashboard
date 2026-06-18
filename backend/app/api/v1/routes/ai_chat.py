from fastapi import APIRouter, HTTPException
from app.schemas.schemas import AIChatRequest, AIChatResponse
from app.core.config import settings
import anthropic

router = APIRouter()

SYSTEM_PROMPT = """Você é um assistente especialista no Clube de Regatas do Flamengo.
Conhece profundamente a história do clube, todos os esportes que pratica (futebol, basquete,
natação, vôlei, remo, eSports, futsal), títulos, jogadores históricos e atuais.
Responda sempre em português brasileiro, de forma direta e precisa, em até 3 parágrafos."""


@router.post("/chat", response_model=AIChatResponse)
async def ai_chat(request: AIChatRequest):
    if not settings.ANTHROPIC_API_KEY:
        raise HTTPException(status_code=503, detail="Anthropic API key não configurada")

    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    messages = [{"role": "user", "content": request.question}]
    if request.context:
        messages[0]["content"] = f"Contexto: {request.context}\n\n{request.question}"

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    return AIChatResponse(
        answer=response.content[0].text,
        tokens_used=response.usage.input_tokens + response.usage.output_tokens,
    )


@router.get("/summary/{sport}")
async def sport_summary(sport: str):
    if not settings.ANTHROPIC_API_KEY:
        raise HTTPException(status_code=503, detail="Anthropic API key não configurada")

    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": f"Faça um breve resumo do desempenho atual do Flamengo no {sport}, "
                       f"em até 2 parágrafos curtos."
        }],
    )
    return {"sport": sport, "summary": response.content[0].text}
