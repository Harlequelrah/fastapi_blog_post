from elrahapi.user import  model
from fastapi_blog_post.settings import authentication
class UserBaseModel(model.UserBaseModel):
    pass

class UserCreateModel(model.UserCreateModel):
    pass

class UserUpdateModel(model.UserUpdateModel):
    pass


class UserReadModel(UserBaseModel):
    class Config :
        from_attributes=True

authentication.UserReadModel = UserReadModel
authentication.UserCreateModel = UserCreateModel
authentication.UserUpdateModel = UserUpdateModel


