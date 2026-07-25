from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer("""🎬 <b>Assalomu alaykum!</b>

Kino olamiga xush kelibsiz! Bu yerda minglab kinolarni bir necha soniyada topishingiz mumkin.

<b>📌 Qanday ishlatish kerak?</b>

Kino kodini yuboring — bot sizga darhol filmni topib beradi.

<i>Masalan:</i> <code>123</code>

<b>💡 Qayerdan kod topaman?</b>
Kodlar bizning kanalimizda joylashgan 👇

📢 Kanal: @sirli_kino

<i>Kod bilmasangiz — kanalga o'ting, u yerda barcha kinolar kodi bilan joylashtirilgan.</i>

Xo'sh, boshladikmi? 🍿""", parse_mode="html")