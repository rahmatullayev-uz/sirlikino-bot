from aiogram import Bot, Dispatcher

import logging
import asyncio

from config.env import TOKEN
from bot.handlers.users.start_command import router as start_command_router

bot = Bot(TOKEN)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

async def root():
    dp = Dispatcher()
    dp.include_router(start_command_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.info("Bot muvaffaqiyatli ishga tushirildi")
    asyncio.run(root())