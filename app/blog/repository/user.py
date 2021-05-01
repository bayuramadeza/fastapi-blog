from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException, status
from blog.hashing import Hash
from blog.repository import user

def create(request: schemas.User, db: Session):
    user = models.User(name= request.name, email= request.email, password= Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with the id {id} is not available"
         )
    return user
    