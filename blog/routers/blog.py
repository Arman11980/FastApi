from fastapi import APIRouter,Depends,status
from blog.schemas import UpdateBlog, CreateBlog
from sqlalchemy.orm import Session
from blog.backend.db import get_db
from blog.repository import blog


router = APIRouter(tags=["blog"],prefix = "/blogs")

@router.post('/create', response_model=CreateBlog,status_code = status.HTTP_201_CREATED,summary="Create a Blog Posts")
def create_post(request:CreateBlog,db:Session = Depends(get_db)):
    return blog.create_post(request,db)

@router.get('/')
def get_all(db:Session = Depends(get_db)):
    return blog.get_all(db)

@router.put('/update/{id}',response_model=UpdateBlog, status_code = status.HTTP_202_ACCEPTED,summary="Update a Blog Posts")
def update_post(id,request:UpdateBlog,db:Session = Depends(get_db)):
    return blog.update_post(id,request,db)

@router.delete('/delete/{id}', status_code = status.HTTP_204_NO_CONTENT,summary="Delete a Blog Posts")
def delete_post(id,db:Session = Depends(get_db)):
    return blog.delete_post(id,db)