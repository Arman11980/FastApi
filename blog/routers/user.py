from fastapi import APIRouter,Depends,status
from blog.schemas import CreateUser
from sqlalchemy.orm import Session
from blog.backend.db import get_db
from blog.repository import user

router = APIRouter(tags=["Users"],prefix = "/users")

@router.post('/create',response_model=CreateUser, status_code = status.HTTP_201_CREATED,summary="Create User Account")
def create_user(request:CreateUser,db:Session = Depends(get_db)):
    return user.create_user(request,db)

@router.get('/get_all', status_code = status.HTTP_200_OK,summary="Get All Users")
def get_all_user(db:Session = Depends(get_db)):
    return user.get_all_user(db)

@router.get('/{id}',status_code = status.HTTP_200_OK,summary="Get User by Id")
def get_user(id,db:Session = Depends(get_db)):
    return user.get_user(id,db)

@router.get('/{username}', status_code = status.HTTP_200_OK,summary="Get User by Username")
def get_username(username:str,db:Session = Depends(get_db)):
    return user.get_username(username,db)