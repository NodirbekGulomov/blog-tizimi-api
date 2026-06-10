from datetime import datetime

from pydantic import BaseModel


class UserProfileResponse(BaseModel):
    id: int
    first_name: str
    last_name: str | None
    email: str
    created_at: datetime
