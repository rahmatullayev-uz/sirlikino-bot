from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
    [
        KeyboardButton(text="🎬 Kinolar "),
        KeyboardButton(text="📊 Statistika")
    ], [
        KeyboardButton(text="📢 Xabar yuborish"),
        KeyboardButton(text="⚙️ Sozlamalar")
    ], [
        KeyboardButton(text="👤 Adminlar"),
        KeyboardButton(text="👥 Foydalanuvchilar")
    ]
])


manage_movie_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="➕ Kino qo'shish"),
            KeyboardButton(text="🗑 Kino o'chirish")
        ], [
            KeyboardButton(text="📋 Kinolar ro'yxati"),
            KeyboardButton(text="🔍 Qidirish")
        ], [
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ]
)

cancel_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ]
)