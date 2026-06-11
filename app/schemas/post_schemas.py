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
