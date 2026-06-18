from sqlalchemy import String, Text, DateTime, Boolean, Integer, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum

from app.core.database import Base


class SportCategory(str, enum.Enum):
    FUTEBOL = "futebol"
    BASQUETE = "basquete"
    NATACAO = "natacao"
    VOLEI = "volei"
    REMO = "remo"
    ESPORTS = "esports"
    FUTSAL = "futsal"
    OUTROS = "outros"


class NewsArticle(Base):
    __tablename__ = "news_articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=True)
    url: Mapped[str] = mapped_column(String(1000), nullable=True)
    source: Mapped[str] = mapped_column(String(200), nullable=True)
    sport: Mapped[SportCategory] = mapped_column(
        Enum(SportCategory), default=SportCategory.FUTEBOL
    )
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False)
    published_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sport: Mapped[SportCategory] = mapped_column(Enum(SportCategory))
    competition: Mapped[str] = mapped_column(String(200))
    round_name: Mapped[str] = mapped_column(String(100), nullable=True)
    opponent: Mapped[str] = mapped_column(String(200))
    flamengo_score: Mapped[int] = mapped_column(Integer, nullable=True)
    opponent_score: Mapped[int] = mapped_column(Integer, nullable=True)
    is_home: Mapped[bool] = mapped_column(Boolean, default=True)
    venue: Mapped[str] = mapped_column(String(300), nullable=True)
    match_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
