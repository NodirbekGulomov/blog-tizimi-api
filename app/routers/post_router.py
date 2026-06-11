from fastapi import APIRouter, Depends

from app.dependencies.auth_dependency import get_current_user
from app.dependencies.db_dependency import get_db
from app.schemas.auth_schemas import CurrentUser
from app.schemas.post_schemas import PostRequest, PostResponse
from app.services import post_service

router = APIRouter(tags=["Post router"])


@router.post("/posts")
def create_post(
    data: PostRequest,
    current_user: CurrentUser = Depends(get_current_user),
    db=Depends(get_db),
):
    return post_service.create_post(data, current_user.id, db)


@router.get("/posts", response_model=list[PostResponse])
def get_all_posts(
    current_user: CurrentUser = Depends(get_current_user),
    db=Depends(get_db),
):
    return post_service.get_all_posts(current_user.id, db)
