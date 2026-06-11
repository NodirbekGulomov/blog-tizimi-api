from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db import Post, User
from app.schemas.post_schemas import PostRequest, PostUpdateRequest


def create_post(data: PostRequest, user_id: int, db: Session):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    post_data = data.model_dump()
    post_data["author_id"] = user_id

    db.add(Post(**post_data))
    db.commit()

    return {"message": "Post created"}


def get_all_posts(user_id: int, db: Session):
    user = db.execute(select(Post).where(Post.author_id == user_id)).scalars()

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")
    return user


def get_post(post_id: int, db: Session):
    post = db.execute(select(Post).where(Post.id == post_id)).scalar_one_or_none()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


def update_post(post_id: int, data: PostUpdateRequest, user_id: int, db: Session):
    post = db.execute(select(Post).where(Post.id == post_id)).scalar_one_or_none()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.author_id != user_id:
        raise HTTPException(status_code=403)

    update_data = data.model_dump(exclude_unset=True)
    update_data.pop("author_id", None)

    for key, value in update_data.items():
        setattr(post, key, value)

    post.updated_at = datetime.now()

    db.commit()
    db.refresh(post)

    return {"message": "Post updated"}
