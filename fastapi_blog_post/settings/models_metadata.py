from fastapi_blog_post.blog_post.models import BlogPost

from fastapi_blog_post.settings.auth.models import (  # LogModel,
    Role,
    RolePrivilege,
    User,
    UserPrivilege,
    UserRole,
)
from fastapi_blog_post.settings.logger.model import LogModel
from fastapi_blog_post.settings.database import Base, database  # à importer en dernier

database.create_tables(target_metadata=Base.metadata)
