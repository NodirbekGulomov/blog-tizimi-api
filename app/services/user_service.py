from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import User
from app.schemas.user_schemas import UserProfileResponse


def get_user_by_id(user_id: int, db: Session):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    return user
