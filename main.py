from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import pydantic
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 2},
            {"title": "title of post 3", "content": "content of post 3", "id": 3}
            ]


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i


@app.get("/")
def root():
    return{"message": "Welcome to my API!"}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(posts: Post):
    post_dict = posts.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return{"data": post_dict}


@app.get("/posts")
def get_posts():
    return{"data": my_posts}


@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return{"data": post}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    return{"data": post}


# @app.put("/posts/{id}")

@app.delete("/posts/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} was not found")
    my_posts.pop(index)
    # return{"message":f"post id {id} was successfully deleted"}
    return Response(status_code=HTTP_204_NO_CONTENT)