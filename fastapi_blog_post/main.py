from fastapi import FastAPI
from elrahapi.middleware.log_middleware import LoggerMiddleware
from fastapi_blog_post.settings.database import engine, authentication
from fastapi_blog_post.settings.models_metadata import target_metadata
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from fastapi_blog_post.blog_post.router import app_blog_post
from fastapi_blog_post.loggerapp.log_router import app_logger
from fastapi_blog_post.userapp.user_routers import app_privilege,app_role,app_role_privilege,app_user_privilege,app_user
from fastapi_blog_post.loggerapp.log_model import Logger
app = FastAPI()

target_metadata.create_all(bind=engine)

@app.get("/")
async def hello():
    return {"message":"hello"}
app.include_router(app_blog_post)
app.include_router(app_logger)
app.include_router(app_user)
app.include_router(app_privilege)
app.include_router(app_role)
app.include_router(app_role_privilege)
app.include_router(app_user_privilege)
app.add_middleware(
    ErrorHandlingMiddleware,
    LoggerMiddlewareModel=Logger,
    session_factory=authentication.session_factory
)

app.add_middleware(
    LoggerMiddleware,
    LoggerMiddlewareModel=Logger,
    session_factory=authentication.session_factory

)
