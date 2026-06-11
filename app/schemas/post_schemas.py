from datetime import datetime

from pydantic import BaseModel


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime | None
    author_id: int


class PostRequest(BaseModel):
    title: str
    content: str


class PostUpdateRequest(BaseModel):
    title: str | None = None
    content: str | None = None
