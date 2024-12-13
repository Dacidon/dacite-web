from article_model import Article
from db.db_init import Base
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy import Text, String, DateTime, ForeignKey

class Author(Base):
    __tablename__ = "author"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(50))
    
    article: Mapped[list["Article"]] = relationship(back_populates="author")