from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging

from handlers import include_routers
from data import Tables
from config import TelegramConfig


async def main():
    Tables.create_tables()
    bot = Bot(token=TelegramConfig.BOT_TOKEN, parse_mode="html")
    dp = Dispatcher(storage=MemoryStorage())
    include_routers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except asyncio.exceptions.CancelledError:
        print("The polling cycle was interrupted")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
