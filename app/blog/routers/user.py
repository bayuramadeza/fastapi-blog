from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import schemas, database, models
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUserWithBlogs)
def show(id, db: Session = Depends(get_db)):
    return user.show(id, db)