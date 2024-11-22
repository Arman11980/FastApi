from sqlalchemy import creat_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = creat_engine('sqlite:///database.db', echo= True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()