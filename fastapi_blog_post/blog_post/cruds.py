from elrahapi.crud.crud_forgery import CrudForgery
from elrahapi.crud.crud_models import CrudModels
from blog_post.models import BlogPost  # remplacer par l'entité SQLAlchemy
from blog_post.schemas import (  # remplacer par les modèles Pydantic
    BlogPostCreateModel,
    BlogPostFullReadModel,
    BlogPostPatchModel,
    BlogPostReadModel,
    BlogPostUpdateModel,
)
from settings.database import database

blog_post_crud_models = CrudModels(
    entity_name="blog_post",
    primary_key_name="id",  # remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=BlogPost,  # remplacer par l'entité SQLAlchemy
    ReadModel=BlogPostReadModel,
    CreateModel=BlogPostCreateModel,  # Optionel
    UpdateModel=BlogPostUpdateModel,  # Optionel
    PatchModel=BlogPostPatchModel,  # Optionel
    FullReadModel=BlogPostFullReadModel,  # Optionel
)
blog_post_crud = CrudForgery(
    crud_models=blog_post_crud_models, session_manager=database.session_manager
)
