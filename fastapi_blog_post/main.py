from blog_post.router import blog_post_router
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from settings.auth.configs import authentication_router
from settings.auth.routers import role_router, user_role_router, user_router

# from myapp.router import myapp_router
from settings.database import database

from fastapi import FastAPI

app = FastAPI(root_path="/api")
app.include_router(authentication_router)
app.include_router(blog_post_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(user_role_router)


@app.get("/")
async def hello():
    return {"message": "hello"}


# app.include_router(myapp_router)
app.add_middleware(
    ErrorHandlingMiddleware,
)
