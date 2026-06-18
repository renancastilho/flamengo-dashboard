from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.api.v1.routes import news, matches, sports, ai_chat, auth
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Flamengo Dashboard API",
    description="API REST para o Dashboard de Notícias do Flamengo — todos os esportes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:80"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router,    prefix="/api/v1/auth",    tags=["auth"])
app.include_router(news.router,    prefix="/api/v1/news",    tags=["news"])
app.include_router(matches.router, prefix="/api/v1/matches", tags=["matches"])
app.include_router(sports.router,  prefix="/api/v1/sports",  tags=["sports"])
app.include_router(ai_chat.router, prefix="/api/v1/ai",      tags=["ai"])


@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok", "service": "Flamengo Dashboard API", "version": "1.0.0"}
