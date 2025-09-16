from pydantic import BaseModel, Field

from blog_post.enums import Status

class BlogPostBaseModel(BaseModel):
    title: str = Field(example="debut de angular")
    content: str = Field(example="je débute avec le framework angular")
    status: Status = Field(example=Status.NOT_STARTED)


# class BlogPostInBlogPost2Model(BaseModel):
#     pass
