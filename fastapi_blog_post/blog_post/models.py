from blog_post.utils import Status
from fastapi_blog_post.settings.database import Base
from sqlalchemy import (
    DECIMAL,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class BlogPost(Base):
    __tablename__ = "blogposts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), nullable=False)
    content = Column(Text, nullable=False)
    status = Column(Enum(Status), default=Status.NOT_STARTED)
    views = Column(Integer, default=0)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)
    date_deleted = Column(DateTime, nullable=True)
