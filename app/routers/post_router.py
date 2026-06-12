from fastapi import APIRouter, Depends

from app.dependencies.auth_dependency import get_current_user
from app.dependencies.db_dependency import get_db
from app.schemas.auth_schemas import CurrentUser
from app.schemas.post_schemas import PostRequest, PostResponse, PostUpdateRequest
from app.services import post_service

router = APIRouter(tags=["Post router"])


@router.post("/posts", status_code=201, response_model=PostResponse)
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


@router.get("/posts/{id}", response_model=PostResponse)
def get_post(
    id: int,
    current_user: CurrentUser = Depends(get_current_user),
    db=Depends(get_db),
):
    return post_service.get_post(id, current_user.id, db)


@router.patch("/posts/{id}", response_model=PostResponse)
def update_post(
    id: int,
    data: PostUpdateRequest,
    db=Depends(get_db),
):
    return post_service.update_post(id, data, db)


@router.delete("/posts/{id}", status_code=204)
def delete_post(
    id: int,
    current_user: CurrentUser = Depends(get_current_user),
    db=Depends(get_db),
):
    return post_service.delete_post(id, current_user.id, db)


@router.get("/posts/search", response_model=list[PostResponse])
def search_posts(post_title: str, db=Depends(get_db)):
    return post_service.search_posts(post_title, db)
