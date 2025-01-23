from fastapi_blog_post.blog_post.models import metadata as myapp_metadata
from fastapi_blog_post.loggerapp.log_model import metadata as myapp2_metadata
from fastapi_blog_post.userapp.user_models import metadata as myapp3_metadata
from sqlalchemy import MetaData
from .database import Base
target_metadata = MetaData()

target_metadata = Base.metadata
target_metadata = myapp_metadata
target_metadata = myapp2_metadata
target_metadata = myapp3_metadata
