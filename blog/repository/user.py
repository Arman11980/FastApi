from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from blog.models import User
from blog.schemas import CreateUser

def create_user(request:CreateUser,db:Session):
    new_user = User(username=request.username,email=request.email,password=request.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int,db:Session):
    user = db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")

    return user

def get_username(username:str,db:Session):
    users = db.query(User).all()
    for user in users :
        if user.username == username :
            return user
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with Username {username} is not available")


def get_all_user(db:Session):
    users = db.query(User).all()
    return users