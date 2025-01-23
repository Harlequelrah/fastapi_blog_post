from elrahapi.router.route_config import  RouteConfig
from fastapi_blog_post.settings.database import authentication
from fastapi_blog_post.blog_post.cruds import blog_post_crud
from fastapi_blog_post.blog_post.schemas import BlogPostPydanticModel
from typing import List
from elrahapi.router.router_provider import CustomRouterProvider

router_provider = CustomRouterProvider(
    prefix="/blog_posts",
    tags=["blog_post"],
    PydanticModel=BlogPostPydanticModel,
    crud=blog_post_crud
)

app_blog_post = router_provider.get_public_router()
# app_todolist = router_provider.get_protected_router()

# init_data: List[RouteConfig] = [
#     RouteConfig(route_name="create", is_activated=True),
#     RouteConfig(route_name="read-one", is_activated=True),
#     RouteConfig(route_name="update", is_activated=True, is_protected=True),
#     RouteConfig(route_name="delete", is_activated=True, is_protected=True),
# ]
# app_myapp = router_provider.initialize_router(init_data=init_data)
