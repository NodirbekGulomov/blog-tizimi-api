from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Comment, Post
from app.schemas.comment_schemas import CommentRequest


def create_comment(post_id: int, data: CommentRequest, user_id: int, db: Session):
    post = db.execute(select(Post).where(Post.id == post_id)).scalar_one_or_none()

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    comment_data = data.model_dump()
    comment_data["post_id"] = post_id
    comment_data["author_id"] = user_id
    comment_object = Comment(**comment_data)

    db.add(comment_object)
    db.commit()

    return {"message": "Comment created"}
