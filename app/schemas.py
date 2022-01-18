from pydantic import BaseModel, EmailStr
from pydantic.networks import EmailStr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserDetails(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserDetails

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token : str
    token_type : str


class TokenData(BaseModel):
    id: Optional[str] = None
