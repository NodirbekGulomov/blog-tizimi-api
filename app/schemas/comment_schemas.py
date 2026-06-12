from datetime import datetime

from pydantic import BaseModel


class CommentResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    author_id: int
    post_id: int


class CommentRequest(BaseModel):
    content: str
