from blog.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__= "user"
    id = Column(Integer(), primary_key=True)
    email = Column(String(200), unique=True)
    username = Column(String(100),unique=True)
    password =Column(String(20))
    blogs= relationship('BlogPost',back_populates = "creator")

    def __repr__(self):
        return f"User {self.username}"
