from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.db.models import Comment, Post
from app.schemas.comment_schemas import CommentRequest, CommentResponse


def create_comment(post_id: int, data: CommentRequest, user_id: int, db: Session):
    post = db.get(Post, post_id)

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    comment_data = data.model_dump()
    comment_data["post_id"] = post_id
    comment_data["author_id"] = user_id
    comment_object = Comment(**comment_data)

    db.add(comment_object)
    db.commit()

    return comment_object


def delete_comment(comment_id: int, user_id: int, db: Session):
    comment = db.get(Comment, comment_id)

    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.author_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    db.delete(comment)
    db.commit()

    return
