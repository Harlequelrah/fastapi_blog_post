from elrahapi.router.router_namespace import DefaultRoutesName
from elrahapi.router.router_provider import CustomRouterProvider
from .log_crud import logCrud
from .log_schema import LoggerMiddlewareReadModel as LMPD

router_provider = CustomRouterProvider(
    prefix="/logs",
    tags=["logs"],
    PydanticModel=LMPD,
    crud=logCrud,
    privileges=["CAN_ADD_PRIVILEGE"]
)
app_logger = router_provider.get_protected_router(
    [DefaultRoutesName.UPDATE, DefaultRoutesName.DELETE, DefaultRoutesName.CREATE]
)
