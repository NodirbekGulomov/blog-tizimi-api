from pydantic import BaseModel


class CurrentUser(BaseModel):
    id: int


class SignUpResponse(BaseModel):
    access_token: str
    refresh_token: str


class SignUpRequest(BaseModel):
    first_name: str
    last_name: str | None = None
    email: str
    password: str


class SignInResponse(BaseModel):
    access_token: str
    refresh_token: str


class SignInRequest(BaseModel):
    email: str
    password: str
