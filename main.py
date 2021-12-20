# Python
from typing import Optional
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List
# Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI, status

app = FastAPI()

#Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50)
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50)
    birthday: Optional[date] = Field(default=None)

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
class Tweet(BaseModel):
    Tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=280
        )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path Operations

## Users

### Register a user
@app.post(
    path = '/signup',
    response_model = User,
    status_code = status.HTTP_201_CREATED,
    summary = "Register a user",
    tags = ["Users"]
)
def signup():
    """
    This path operation register a user in the app

    Parameters: 
        - Request body parameter
            -user: UserRegister
    
    Returns a json with the basic user information:
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birthday: date
    """
    pass

### Login a user
@app.post(
    path = '/login',
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Login a user",
    tags = ["Users"]
)
def login():
    pass

### Show all users
@app.get(
    path = '/users',
    response_model = List[User],
    status_code = status.HTTP_200_OK,
    summary = "Show all users",
    tags = ["Users"]
)
def show_all_users():
    pass

### Show a user
@app.get(
    path = '/users/{id}',
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Show a user",
    tags = ["Users"]
)
def show_user():
    pass

### Delete a user
@app.delete(
    path = '/users/{id}',
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Delete a user",
    tags = ["Users"]
)
def delete_user():
    pass

### Update a user
@app.put(
    path = '/users/{id}',
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Update a user",
    tags = ["Users"]
)
def update_user():
    pass


## Tweets

### Show all tweets
@app.get(
    path = '/',
    response_model = List[Tweet],
    status_code = status.HTTP_200_OK,
    summary = "Show all tweets",
    tags = ["Tweets"]
)
def home():
    return {"Twitter API": "Working"}

### Post a tweet
@app.post(
    path = '/post',
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED,
    summary = "Post a tweet",
    tags = ["Tweets"]
)
def post_tweet():
    pass

### Show a tweet
@app.get(
    path = '/tweets/{id}',
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "Show a tweet",
    tags = ["Tweets"]
)
def show_tweet():
    pass

### Delete a tweet
@app.delete(
    path = '/tweets/{id}',
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "Delete a tweet",
    tags = ["Tweets"]
)
def delete_tweet():
    pass

### update a tweet
@app.put(
    path = '/tweets/{id}',
    response_model = Tweet,
    status_code = status.HTTP_200_OK,
    summary = "Update a tweet",
    tags = ["Tweets"]
)
def update_tweet():
    pass