from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "📊 Statistika")
async def stat(message: Message):
    await message.answer(parse_mode="html", text="""📊 <b>Bot statistikasi</b>

👥 Jami foydalanuvchilar: <b>{total_users}</b>
🆕 Bugun qo'shilgan: <b>{today_users}</b>
🎬 Jami kinolar: <b>{total_movies}</b>
🔎 Bugungi so'rovlar: <b>{today_requests}</b>
📈 Eng ko'p so'ralgan kino: <b>{top_movie}</b>""")