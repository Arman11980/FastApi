from blog.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func

class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    author = Column(String(20), nullable=False)
    posted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer(), ForeignKey('user.id'))
    user = relationship('User', back_populates='blog')
    def __repr__(self):
        return f"User {self.title} and BY:{self.author}"

