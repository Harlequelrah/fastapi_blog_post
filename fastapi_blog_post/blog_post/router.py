from elrahapi.router.router_namespace import (
    DefaultRoutesName,
    TypeRoute,
)
from elrahapi.router.router_provider import CustomRouterProvider

from settings.auth.configs import authentication
from blog_post.cruds import blog_post_crud

router_provider = CustomRouterProvider(
    prefix="/blog_posts",
    tags=["blog_post"],
    crud=blog_post_crud,
    # authentication=authentication,
)

blog_post_router = router_provider.get_public_router()
# blog_post_router = router_provider.get_protected_router()

