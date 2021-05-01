from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'data': {
        'name': 'Bayu'
    }}

@app.get('/about')
def about():
    return {'data': 'abuutpage'}

@app.get('/blog')
def show(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} unpublished blogs from db'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'title is {blog.title}'} 