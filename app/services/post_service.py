from datetime import datetime

from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.db import Post, User
from app.schemas.post_schemas import PostRequest, PostResponse, PostUpdateRequest


def create_post(data: PostRequest, user_id: int, db: Session):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication required")

    post_data = data.model_dump()
    post_data["author_id"] = user_id
    post_object = Post(**post_data)

    db.add(post_object)
    db.commit()

    return post_object


def get_all_posts(user_id: int, db: Session):
    user = db.get(User, user_id)
    return user.posts


def get_post(post_id: int, db: Session):
    post = db.get(Post, post_id)

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


def update_post(post_id: int, data: PostUpdateRequest, user_id: int, db: Session):
    post = db.get(Post, post_id)

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.author_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    update_data = data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(post, key, value)

    db.commit()
    db.refresh(post)

    return post


def delete_post(post_id: int, user_id, db: Session):
    post = db.get(Post, post_id)

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.author_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    db.delete(post)
    db.commit()

    return


def search_posts(post_title: str, db: Session):
    stmt = select(Post).where(Post.title.ilike(post_title))
    posts = db.execute(stmt).scalars()
    print('alsdkjfjfdl;ks')

    return posts
