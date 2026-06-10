from fastapi import APIRouter, Depends

from app.dependencies.auth_dependency import get_current_user
from app.dependencies.db_dependency import get_db
from app.schemas.auth_schemas import (
    CurrentUser,
    SignInRequest,
    SignInResponse,
    SignUpRequest,
    SignUpResponse,
)
from app.schemas.user_schemas import UserProfileResponse
from app.services import auth_service, user_service

router = APIRouter()


@router.post("/auth/signup", response_model=SignUpResponse)
def sign_up(data: SignUpRequest, db=Depends(get_db)):
    return auth_service.create_user(data, db)


@router.post("/auth/signin", response_model=SignInResponse)
def sign_in(data: SignInRequest, db=Depends(get_db)):
    return auth_service.handle_sign_in(data, db)


@router.get("/users/me", response_model=UserProfileResponse)
def get_user_profile(
    currentUser: CurrentUser = Depends(get_current_user), db=Depends(get_db)
):
    return user_service.get_user_by_id(currentUser.id, db)
