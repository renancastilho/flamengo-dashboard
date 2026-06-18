from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from app.models.models import SportCategory


class NewsArticleOut(BaseModel):
    id: int
    title: str
    summary: Optional[str]
    url: Optional[str]
    source: Optional[str]
    sport: SportCategory
    is_featured: bool
    published_at: Optional[datetime]
    created_at: datetime

    model_config = {"from_attributes": True}


class NewsArticleCreate(BaseModel):
    title: str
    summary: Optional[str] = None
    url: Optional[str] = None
    source: Optional[str] = None
    sport: SportCategory = SportCategory.FUTEBOL
    is_featured: bool = False
    published_at: Optional[datetime] = None


class MatchOut(BaseModel):
    id: int
    sport: SportCategory
    competition: str
    round_name: Optional[str]
    opponent: str
    flamengo_score: Optional[int]
    opponent_score: Optional[int]
    is_home: bool
    venue: Optional[str]
    match_date: datetime
    is_completed: bool
    result: Optional[str] = None

    model_config = {"from_attributes": True}

    @classmethod
    def from_orm_with_result(cls, obj):
        data = cls.model_validate(obj)
        if obj.is_completed and obj.flamengo_score is not None:
            if obj.flamengo_score > obj.opponent_score:
                data.result = "V"
            elif obj.flamengo_score < obj.opponent_score:
                data.result = "D"
            else:
                data.result = "E"
        return data


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AIChatRequest(BaseModel):
    question: str
    context: Optional[str] = None


class AIChatResponse(BaseModel):
    answer: str
    tokens_used: int
