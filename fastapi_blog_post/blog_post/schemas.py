from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

from .meta_models import BlogPostBaseModel, Status


class BlogPostCreateModel(BlogPostBaseModel):
    pass


class BlogPostUpdateModel(BlogPostBaseModel):
    views: int = Field(example=2)


class BlogPostPatchModel(BaseModel):
    title: str | None = Field(example="debut de angular", default=None)
    content: str | None = Field(
        example="je débute avec le framework angular", default=None
    )
    status: Status = Field(example=Status.NOT_STARTED, default=Status.NOT_STARTED)
    views: int | None = Field(example=2, default=None)


class BlogPostReadModel(BlogPostBaseModel):
    id: int
    views: int
    date_created: datetime
    date_updated: datetime
    date_deleted: datetime | None = None
    is_deleted: bool
    model_config = ConfigDict(from_attributes=True)


class BlogPostFullReadModel(BlogPostReadModel):
    model_config = ConfigDict(from_attributes=True)
