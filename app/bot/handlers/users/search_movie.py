from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text.regexp(r"^[1-9]\d*$"))
async def analyze_code(message: Message):
    await message.answer("Salom, kod qabul qilindi!")