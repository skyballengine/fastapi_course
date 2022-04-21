from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# Schemas/Pydantic Models

# Original, one single class for Posts that inherits from BaseModel
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True

# Post Base Class, that all other classes inherit from
# Inherits from BaseModel
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    # leaves it the same as it's parent
    pass


class PostUpdate(BaseModel):
    # only allows user to change the content and whether it's published or not
    content: str
    published: bool


# Above PostResponse where it is used
class UsersResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class VoteResponse(BaseModel):
    votes: int
    message: str

    class Config:
        orm_mode = True


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UsersResponse

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True


# Users of the application
class UserCreate(BaseModel):
    email: EmailStr
    password: str


# user login schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserLoginResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True


# schema for jwt token
class Token(BaseModel):
    access_token: str
    token_type: str


# schema for data payload of token
class TokenData(BaseModel):
    id: Optional[str] = None


# schema for voting
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
