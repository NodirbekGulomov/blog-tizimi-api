from fastapi import APIRouter, Depends

from app.dependencies.db_dependency import get_db
from app.schemas.auth_schemas import SignupRequest, SignupResponse
from app.services import auth_service

router = APIRouter()


@router.post("/signup", response_model=SignupResponse)
def sign_up(data: SignupRequest, db=Depends(get_db)):
    return auth_service.create_user(data, db)
