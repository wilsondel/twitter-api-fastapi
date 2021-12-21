# Python
import json
from typing import Optional
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI, status,Body,HTTPException

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
    birthdate: Optional[date] = Field(default=None)

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )
class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
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
def signup(
    user: UserRegister = Body(...)
):
    """
    Signup

    This path operation register a user in the app

    Parameters: 
    - Request body parameter
        - user: UserRegister
    
    Returns a json with the basic user information:
    - user_id: UUID
    - email: Emailstr
    - first_name: str
    - last_name: str
    - birthdate: date
    """
    with open("users.json","r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict=user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birthdate"] = str(user_dict["birthdate"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user

### Login a user
@app.post(
    path = '/login',
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Login a user",
    tags = ["Users"]
)
def login(
    user: UserRegister = Body(...)
):
    """
    Login

    This path operation login a user in the app

    Parameters: 
    - Request body parameter
        - user: UserRegister
    
    Returns a json with the basic user information (if user exists):
    - user_id: UUID
    - email: Emailstr
    - first_name: str
    - last_name: str
    - birthdate: date
    otherwise raise an HTTP exception with status code 404.
    """
    with open("users.json","r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict=user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birthdate"] = str(user_dict["birthdate"])
        print(results)
        for u in results:
            if u["email"] == user_dict["email"]:
                return user
    raise HTTPException(status_code=404, detail="User not found")

### Show all users
@app.get(
    path = '/users',
    response_model = List[User],
    status_code = status.HTTP_200_OK,
    summary = "Show all users",
    tags = ["Users"]
)
def show_all_users():
    """
    This path operation shows all users in the app

    Parameters:
    -

    Returns a json list with all users in the app, with the following keys
    - user_id: UUID
    - email: Emailstr
    - first_name: str
    - last_name: str
    - birthdate: date

    """
    with open("users.json","r", encoding="utf-8") as f:
        results=json.loads(f.read())
        return results


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
    """
    This path operation shows all tweets in the app

    Parameters:
    -/

    Returns a json with the basic tweet information:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json","r", encoding="utf-8") as f:
        results=json.loads(f.read())
        return results


### Post a tweet
@app.post(
    path = '/post',
    response_model = Tweet,
    status_code = status.HTTP_201_CREATED,
    summary = "Post a tweet",
    tags = ["Tweets"]
)
def post_tweet(
    tweet: Tweet = Body(...)
):
    """
    Post a tweet

    This path operation post a tweet in the app

    Parameters: 
    - Request body parameter
        - tweet: Tweet
    
    Returns a json with the basic tweet information:
    - tweet_id: UUID
    - content: str
    - created_at: datetime
    - updated_at: Optional[datetime]
    - by: User
    """
    with open("tweets.json","r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict=tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birthdate"] = str(tweet_dict["by"]["birthdate"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

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