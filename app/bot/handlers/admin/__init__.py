from aiogram import Router

from .sign_in_admin import router as sign_in_router
from .movies import router as movie_router
from .stat import router as stat_router

router = Router()

router.include_routers(
    sign_in_router,
    movie_router,
    stat_router
)