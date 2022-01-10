from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import pydantic

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 2}
            ]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

@app.get("/")
def root():
    return{"message": "Welcome to my API!"}


@app.post("/posts")
def create_post(posts: Post):
    post_dict = posts.dict()
    post_dict['id'] = randrange(0,10000000)
    my_posts.append(post_dict)
    return{"data": post_dict}



@app.get("/posts")
def get_posts():
    return{"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    print(post)
    return{"post_detail":post}


# @app.put("/posts/{id}")

# @app.delete("/posts/{id}")
