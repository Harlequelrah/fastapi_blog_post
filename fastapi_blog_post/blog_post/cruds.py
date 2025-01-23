from fastapi_blog_post.blog_post.models import BlogPost
from fastapi_blog_post.blog_post.schemas import BlogPostCreatePydanticModel, BlogPostUpdatePydanticModel
from elrahapi.crud.crud_forgery import CrudForgery
from fastapi_blog_post.settings.database import authentication

blog_post_crud = CrudForgery(
    entity_name="blog_post",
    authentication=authentication,
    SQLAlchemyModel=BlogPost,
    CreatePydanticModel=BlogPostCreatePydanticModel,
    UpdatePydanticModel=BlogPostUpdatePydanticModel,
)
