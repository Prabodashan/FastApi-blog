from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str]=None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blog from the'}
    else:
        return {'data': f'{limit} blog from the'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs' }

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    #fetch comments of blog with id = id
    return{'data': {'1', '2'}}