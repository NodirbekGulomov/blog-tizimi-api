from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import Post, User
from app.schemas.post_schemas import PostRequest


def create_post(data: PostRequest, author_id: int, db: Session):
    user = db.execute(select(User).where(User.id == author_id)).scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    post_data = data.model_dump()
    post_data["author_id"] = author_id

    db.add(Post(**post_data))
    db.commit()

    return {"message": "Post created"}


def get_all_posts(user_id: int, db: Session):
    user = db.execute(select(Post).where(Post.author_id == user_id)).scalars()

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    return user
