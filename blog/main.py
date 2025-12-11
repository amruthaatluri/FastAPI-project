from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code= status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session= Depends(get_db)):
    new_blog=models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", response_model=List[schemas.Showonly])
def all(db:Session= Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get("/blogs/{id}", status_code=200, response_model=schemas.Showonly)
def show(id,db:Session= Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= 'id not available')

    return blog

@app.delete("/blogs/{id}")
def delete(id,db:Session= Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog {id} not found to update")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"

@app.put("/blogs/{id}")
def update(id,request:schemas.Blog, db:Session= Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog {id} not found to delete")
    blog.update(request.dict())
    db.commit()
    return "updated"




@app.post("/blogs")
def create_user(request: schemas.User, db:Session= Depends(get_db) ):
    
    new_user=models.User(name=request.name, email=request.email, password= Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user