from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import (
    create_jwt_access_token,
    create_jwt_refresh_token,
    hash_password,
)
from app.db import User
from app.schemas.auth_schemas import SignupRequest


def create_user(data: SignupRequest, db: Session):
    user = db.execute(
        select(User.email).where(User.email == data.email)
    ).scalar_one_or_none()

    if user:
        raise HTTPException(status_code=409, detail="Email already exists")

    data = data.model_dump()
    data["hashed_password"] = hash_password(data.pop("password"))

    user_object = User(**data)

    db.add(user_object)
    db.commit()

    access_token_data = {"id": user_object.id}

    return {
        "access_token": create_jwt_access_token(access_token_data),
        "refresh_token": create_jwt_refresh_token(user_object.id),
    }
