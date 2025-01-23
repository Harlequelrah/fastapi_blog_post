from elrahapi.crud.crud_forgery import CrudForgery
from fastapi_blog_post.settings.database import authentication
from .log_model import Logger

logCrud = CrudForgery(
    entity_name="log",
    SQLAlchemyModel=Logger,
    authentication=authentication,
)
