from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from blog.models import Blog
from blog.schemas import UpdateBlog,CreateBlog

def get_all(db:Session):
    blogs = db.query(Blog).all()
    return blogs

def create_post(request:CreateBlog,db:Session):
    new_blog = Blog(title=request.title,content=request.content,author=request.author,user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_post(id:int,db:Session):
    post_delete = db.query(Blog).filter(Blog.id == id).first()

    if post_delete  is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resources not Found")
    else:
        db.delete(post_delete)
        db.commit()

    return f"Blog Post with id {id} has been successfully deleted."

def update_post(id:int,request:UpdateBlog,db:Session):
    post_update = db.query(Blog).filter(Blog.id == id).first()
    post_update.title = request.title
    post_update.content = request.content

    if post_update  is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resources not Found")
    else:
        db.commit()

    return post_update