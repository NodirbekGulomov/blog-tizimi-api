from pydantic import BaseModel


class SignupResponse(BaseModel):
    access_token: str
    refresh_token: str


class SignupRequest(BaseModel):
    first_name: str
    last_name: str | None = None
    email: str
    password: str
