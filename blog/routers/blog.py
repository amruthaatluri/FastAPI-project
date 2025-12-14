from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import database, models, schemas
from sqlalchemy.orm import Session
from ..repository import blog
from . import oauth2
router= APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

get_db= database.get_db

@router.get("/", response_model=List[schemas.Showblog])
def all(db:Session= Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    
    return blog.get_all(db)

@router.post("/", status_code= status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session= Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get("/{id}", status_code=200, response_model=schemas.Showblog)
def show(id,db:Session= Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
   
    return blog.show(id,db)

@router.delete("/{id}")
def delete(id,db:Session= Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):

    return blog.destroy(id,db)

@router.put("/{id}")
def update(id,request:schemas.Blog, db:Session= Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
  
    return blog.update(id,request,db)
