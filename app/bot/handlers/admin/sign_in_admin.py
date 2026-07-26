from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards.admin_kb import main_kb

router = Router()

@router.message(Command("panel"))
async def sign_in_admin(message: Message):
    await message.answer("""🛡 <b>Admin panel</b>

Xush kelibsiz! Botni shu yerdan to'liq boshqarishingiz mumkin.

Kerakli bo'limni tanlang 👇""", parse_mode="html", reply_markup=main_kb)


@router.message(F.text == "⬅️ Orqaga")
async def cancel_procces(message: Message):
    await message.answer("""🛡 <b>Admin panel</b>
    
Xush kelibsiz! Botni shu yerdan to'liq boshqarishingiz mumkin.
    
Kerakli bo'limni tanlang 👇""", parse_mode="html", reply_markup=main_kb)