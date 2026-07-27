from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.keyboards.admin_kb import manage_movie_kb, cancel_kb
from bot.states.admin_states import manage_movie_state, RemoveMovie

import logging

router = Router()

@router.message(F.text == "🎬 Kinolar")
async def init_to_movies(message: Message, state: FSMContext):
    await message.answer("""🎬 <b>Kinolar boshqaruvi</b>

Kerakli amalni tanlang:""", parse_mode="html", reply_markup=manage_movie_kb)
    await state.set_state(manage_movie_state.get_file)




@router.message(F.text == "➕ Kino qo'shish")
async def start_movie_process(message: Message, state: FSMContext):
    await message.answer(
        parse_mode="html",
        reply_markup=cancel_kb,
        text="""
🎬 <b>Yangi kino qo'shish</b>

Kino faylini yuboring.
Bot uni qabul qilib, keyingi qadamga o'tadi.

📌 <i>Format:</i> video (.mp4, .mkv)
""")


@router.message(manage_movie_state.get_file)
async def get_movie_file(message: Message, state: FSMContext):
    await state.set_data(name=message.video.file_id)
    await state.set_state(manage_movie_state.get_name)
    await message.answer(
        parse_mode="html",
        reply_markup=cancel_kb,
        text="""
✅ <b>Fayl qabul qilindi!</b>

Endi kino nomini yuboring.

✍️ <i>Namuna:</i>
<code>Titanik (1997)</code>
""")


@router.message(manage_movie_state.get_name)
async def add_movie_name_process(message: Message, state: FSMContext):
    kino_nomi="O'rgimchak odam"
    kino_kodi=45
    await message.answer(
        parse_mode="html",
        reply_markup=manage_movie_kb,
        text=f"""
🎉 <b>Kino muvaffaqiyatli qo'shildi!</b>

🎬 Nomi: <b>{kino_nomi}</b>
🆔 Kodi: <code>{kino_kodi}</code>

Foydalanuvchilar shu kod orqali kinoni topadi. 🍿
""")



@router.message(F.text == "🗑 Kino o'chirish")
async def remove_movie_from_database(message: Message, state: FSMContext):
    await state.set_state(RemoveMovie.get_code)
    await message.answer(
        parse_mode="html",
        reply_markup=cancel_kb,
        text="""
🗑 <b>Kinoni o'chirish</b>

O'chirmoqchi bo'lgan kino kodini yuboring.

🆔 <i>Namuna:</i>
<code>12345</code>
""")


@router.message(RemoveMovie.get_code)
async def remove_movie_from_database_physic(message: Message, state: FSMContext):
    await state.clear()
    kino_nomi = "O'rgimchak odam"
    kino_kodi = 45
    await message.answer(
        parse_mode="html",
        reply_markup=manage_movie_kb,
        text=f"""
✅ <b>Kino o'chirildi!</b>

🎬 Nomi: <b>{kino_nomi}</b>
🆔 Kodi: <code>{kino_kodi}</code>

Ushbu kino botdan butunlay o'chirildi.
""")