from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from fastapi import Form
from .enums import Status

class BlogPostCreatePydanticModel(BaseModel):
    title:str=Field(example="debut de angular")
    content:str=Field(example="je débute avec le framework angular")
    status:Status=Field(example=Status.NOT_STARTED)

class BlogPostUpdatePydanticModel(BaseModel):
    title:Optional[str]=Field(example="debut de angular")
    content:Optional[str]=Field(example="je débute avec le framework angular")
    status:Optional[Status]=Field(example=Status.NOT_STARTED)
    views:Optional[int]=Field(example=2)

class BlogPostPydanticModel(BlogPostCreatePydanticModel):
    id : int
    views:int
