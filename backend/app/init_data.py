from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import engine, Base, AsyncSessionLocal
from app.models.models import NewsArticle, Match, SportCategory


async def init_sample_data():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as db:
        existing_news = await db.execute(select(NewsArticle))
        existing_matches = await db.execute(select(Match))

        if existing_news.scalars().first() and existing_matches.scalars().first():
            print("ℹ️ Dados já existentes — pulando inicialização.")
            return

        sample_news = [
            NewsArticle(
                title="Flamengo vence clássico e assume liderança do Brasileirão",
                summary="Na noite de ontem, o Mengão derrotou o rival por 2x1 no Maracanã.",
                source="GloboEsporte",
                sport=SportCategory.FUTEBOL,
                is_featured=True,
                published_at=datetime.now() - timedelta(hours=2),
            NewsArticle(
                title="Basquete do Flamengo está na final da Champions League Americas",
                summary="Equipe venceu o jogo de volta e garantiu vaga na decisão.",
                source="ESPN",
                sport=SportCategory.BASQUETE,
                is_featured=False,
                published_at=datetime.now() - timedelta(days=1),
            NewsArticle(
                title="Nadador do Flamengo conquista medalha de ouro no Troféu Brasil",
                summary="Atleta bateu recorde pessoal na prova de 100m livre.",
                source="CBDA",
                sport=SportCategory.NATACAO,
                is_featured=False,
                published_at=datetime.now() - timedelta(days=2),
            NewsArticle(
                title="Flamengo de eSports avança na CBLOL",
                summary="Equipe venceu série por 2x0 e está na próxima fase.",
                source="GamingNews",
                sport=SportCategory.ESPORTS,
                is_featured=False,
                published_at=datetime.now() - timedelta(days=2)),
            NewsArticle(
                title="Futsal do Flamengo vence por 5x0 no Campeonato Carioca",
                summary="Grande performance da equipe em casa.",
                source="FlahFutsal",
                sport=SportCategory.FUTSAL,
                is_featured=False,
                published_at=datetime.now() - timedelta(days=3)),
            NewsArticle(
                title="Vôlei masculino do Flamengo faz jogo emocionante",
                summary="Partida terminou em 3x2 para o adversário, mas time mostrou garra.",
                source="Superliga",
                sport=SportCategory.VOLEI,
                is_featured=False,
                published_at=datetime.now() - timedelta(days=4)),
        ]

        sample_matches = [
            Match(
                sport=SportCategory.FUTEBOL,
                competition="Brasileirão Série A",
                round_name="10ª rodada",
                opponent="Vasco",
                flamengo_score=2,
                opponent_score=1,
                is_home=True,
                venue="Maracanã",
                match_date=datetime.now() - timedelta(days=1),
                is_completed=True,
            ),
            Match(
                sport=SportCategory.FUTEBOL,
                competition="Copa do Brasil",
                round_name="Oitavas",
                opponent="Corinthians",
                flamengo_score=1,
                opponent_score=1,
                is_home=False,
                venue="Arena Corinthians",
                match_date=datetime.now() - timedelta(days=3),
                is_completed=True,
            ),
            Match(
                sport=SportCategory.BASQUETE,
                competition="NBB",
                round_name="Playoffs",
                opponent="Franca",
                flamengo_score=85,
                opponent_score=82,
                is_home=True,
                venue="Ginásio do Maracanãzinho",
                match_date=datetime.now() - timedelta(days=2),
                is_completed=True,
            ),
            Match(
                sport=SportCategory.ESPORTS,
                competition="CBLOL",
                round_name="Regular Season",
                opponent="LOUD",
                flamengo_score=2,
                opponent_score=1,
                is_home=True,
                venue="Studio Riot",
                match_date=datetime.now() - timedelta(days=5),
                is_completed=True,
            ),
            Match(
                sport=SportCategory.FUTSAL,
                competition="Campeonato Carioca",
                round_name="6ª rodada",
                opponent="Botafogo",
                flamengo_score=5,
                opponent_score=0,
                is_home=True,
                venue="Ginásio Carioca",
                match_date=datetime.now() - timedelta(days=6),
                is_completed=True,
            ),
            Match(
                sport=SportCategory.FUTEBOL,
                competition="Libertadores",
                round_name="Fase de Grupos",
                opponent="Palmeiras",
                flamengo_score=None,
                opponent_score=None,
                is_home=True,
                venue="Maracanã",
                match_date=datetime.now() + timedelta(days=3),
                is_completed=False,
            ),
            Match(
                sport=SportCategory.BASQUETE,
                competition="Champions League Americas",
                round_name="Final",
                opponent="San Lorenzo",
                flamengo_score=None,
                opponent_score=None,
                is_home=False,
                venue="Arena Buenos Aires",
                match_date=datetime.now() + timedelta(days=7),
                is_completed=False,
            ),
        ]

        db.add_all(sample_news)
        db.add_all(sample_matches)
        await db.commit()
        print("✅ Dados de exemplo adicionados com sucesso!")


if __name__ == "__main__":
    import asyncio
    asyncio.run(init_sample_data())
