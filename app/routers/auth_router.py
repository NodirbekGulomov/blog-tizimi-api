from fastapi import APIRouter, Depends

from app.dependencies.db_dependency import get_db
from app.schemas.auth_schemas import (
    SignInRequest,
    SignInResponse,
    SignUpRequest,
    SignUpResponse,
)
from app.services import auth_service

router = APIRouter()


@router.post("/signup", response_model=SignUpResponse)
def sign_up(data: SignUpRequest, db=Depends(get_db)):
    return auth_service.create_user(data, db)


@router.post("/signin", response_model=SignInResponse)
def sign_in(data: SignInRequest, db=Depends(get_db)):
    return auth_service.handle_sign_in(data, db)
