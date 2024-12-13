from author_model import Author
from db.db_init import Base
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy import Text, String, DateTime, ForeignKey
from datetime import datetime

class Article(Base):
    __tablename__ = "article"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[str] = mapped_column(ForeignKey("author.id"))
    text: Mapped[str] = mapped_column(Text())
    created_at: Mapped[datetime] = mapped_column(DateTime())
    
    author: Mapped["Author"] = relationship(back_populates="article")