from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine

db_engine = create_async_engine("postgresql+psycopg://daciteweb:1952@localhost:5432/daciteWeb")

class Base(DeclarativeBase):
    pass  
