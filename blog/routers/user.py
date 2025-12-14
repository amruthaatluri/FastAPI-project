from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import database, models, schemas
from ..repository import user
from sqlalchemy.orm import Session
router= APIRouter(
    prefix="/user",
tags=["User"]

)
get_db= database.get_db
@router.post("/", response_model=schemas.Showuser)
def create_user(request: schemas.User, db:Session= Depends(get_db) ):
    
    return user.create(request,db)

@router.get("/{id}", response_model=schemas.Showuser, tags=["User"])
def userid(id:int , db:Session= Depends(get_db)):
    
    return user.show(id,db)