from fastapi import APIRouter, Depends

from app.dependencies.auth_dependency import get_current_user
from app.dependencies.db_dependency import get_db
from app.schemas.comment_schemas import CommentRequest
from app.services import comment_service

router = APIRouter(tags=["Comment"])


@router.post("/posts/{id}")
def create_comment(
    id: int,
    data: CommentRequest,
    current_user=Depends(get_current_user),
    db=Depends(get_db),
):
    return comment_service.create_comment(id, data, current_user.id, db)


@router.delete("/comments/{id}", status_code=204)
def delete_comment(
    id: int,
    current_user=Depends(get_current_user),
    db=Depends(get_db),
):
    return comment_service.delete_comment(id, current_user.id, db)
