from aiogram import Router

from .start_command import router as command_start
from .search_movie import router as search_movie

router = Router()
router.include_routers(
    command_start,
    search_movie
)