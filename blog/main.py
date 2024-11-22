from fastapi import FastAPI,Request,Depends,Form,status
from starlette.templating import Jinja2Templates

from routers import blog, user
from sqlalchemy.orm import Session
from blog.backend.db import get_db
from fastapi.responses import HTMLResponse,RedirectResponse
from blog.models import Blog, User

app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.include_router(blog.router)
app.include_router(user.router)



@app.get('/',response_class=HTMLResponse,tags=["Template"])
def posts(request: Request, db:Session = Depends(get_db)):
    users = db.query(User).all()
    blogs = db.query(Blog).all()
    return templates.TemplateResponse("post.html",{"request":request,"users":users,"blogs":blogs})

@app.get('/profile',response_class=HTMLResponse,tags=["Template"])
def users(request: Request, db:Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("profile.html",{"request":request,"users":users})

@app.get('/create_post',response_class=HTMLResponse,tags=["Template"])
def create_post(request: Request):
    return templates.TemplateResponse("new_post.html",{"request":request})

@app.post('/create_post',response_class=HTMLResponse,tags=["Template"])
def create_post(request: Request, db:Session = Depends(get_db),title:str=Form(...),content:str=Form(...),author:str=Form(...),user_id:int=Form(...)):
    errors = []
    try:
        new_blog = Blog(title=title,content=content,author=author,user_id = user_id)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        redirect_url = "/"
        return RedirectResponse(redirect_url,status_code=status.HTTP_303_SEE_OTHER)
    except :
        errors.append("Something went Wrong make sure you are doing the right thing")
        return templates.TemplateResponse("new_post.html",{"request":request,"errors":errors})

@app.get('/edit_post/{id}',response_class=HTMLResponse,tags=["Template"])
def update_post(request: Request,id:int,db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return templates.TemplateResponse("edit.html",{"request":request,"blog":blog})

@app.post('/edit_post/{id}',response_class=HTMLResponse,tags=["Template"])
def update_post(request: Request,id:int, db:Session = Depends(get_db),title:str=Form(...),content:str=Form(...)):
    errors = []
    try:
        update_post = db.query(Blog).filter(Blog.id == id).first()
        update_post.title=title
        update_post.content=content
        db.commit()
        redirect_url = "/"
        return RedirectResponse(redirect_url,status_code=status.HTTP_303_SEE_OTHER)
    except :
        errors.append("Something went Wrong, You are not authorized to edit this post.")
        return templates.TemplateResponse("edit.html",{"request":request,"errors":errors})

@app.get('/delete_post/{id}',tags=["Template"])
def delete_post(request: Request,id:int, db:Session = Depends(get_db)):
    errors= []
    try:
        delete_post = db.query(Blog).filter(Blog.id == id).first()
        db.delete(delete_post)
        db.commit()
        redirect_url = "/"
        return RedirectResponse(redirect_url,status_code=status.HTTP_303_SEE_OTHER)
    except:
        errors.append("Something went Wrong, You are not authorized to delete this Post.")
        return templates.TemplateResponse("post.html",{"request":request,"errors":errors})