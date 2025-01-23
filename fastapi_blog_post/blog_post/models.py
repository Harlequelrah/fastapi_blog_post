from sqlalchemy import (
    Boolean,
    Column,
    DECIMAL,
    Enum,
    Integer,
    Text,
    String,
    DateTime,
    ForeignKey,
    Table,
)
from fastapi_blog_post.settings.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .enums import Status

class BlogPost(Base):
    __tablename__ = 'blogposts'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(30),nullable=False)
    content=Column(Text,nullable=False)
    status=Column(Enum(Status),default=Status.NOT_STARTED)
    views=Column(Integer,default=0)

metadata= Base.metadata
