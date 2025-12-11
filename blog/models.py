from sqlalchemy import Boolean, Integer, Column, ForeignKey, String
from .database import Base
class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    body=Column(String)

class User(Base):
    __tablename__="users"
    id=id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    email=Column(String, nullable=False)
    password= Column(String)
