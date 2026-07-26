from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards.admin_kb import manage_movie_kb

router = Router()

@router.message(F.text == "🎬 Kinolar")
async def init_to_movies(message: Message):
    await message.answer("""🎬 <b>Kinolar boshqaruvi</b>

Kerakli amalni tanlang:""", parse_mode="html", reply_markup=manage_movie_kb)