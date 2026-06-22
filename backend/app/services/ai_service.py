import anthropic
from typing import Optional
from app.core.config import settings
from app.schemas.schemas import AIChatRequest, AIChatResponse

SYSTEM_PROMPT = """Você é um assistente especialista no Clube de Regatas do Flamengo.
Conhece profundamente a história do clube, todos os esportes que pratica (futebol, basquete,
natação, vôlei, remo, eSports, futsal), títulos, jogadores históricos e atuais.
Responda sempre em português brasileiro, de forma direta e precisa, em até 3 parágrafos."""

class AIService:
    def __init__(self):
        self.api_key = settings.ANTHROPIC_API_KEY
        self.client = anthropic.Anthropic(api_key=self.api_key) if self.api_key else None

    def _check_client(self):
        if not self.client or not self.api_key:
            raise ValueError("Anthropic API key não configurada")

    async def get_chat_response(self, question: str, context: Optional[str] = None) -> AIChatResponse:
        self._check_client()
        
        content = question
        if context:
            content = f"Contexto: {context}\n\n{question}"

        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": content}],
        )

        return AIChatResponse(
            answer=response.content[0].text,
            tokens_used=response.usage.input_tokens + response.usage.output_tokens,
        )

    async def get_sport_summary(self, sport: str) -> dict:
        self._check_client()
        
        response = self.client.messages.create(
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
