from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
import os

from handlers import (default_handlers, help_handlers, tutor_handlers, alarm_handlers, command_handlers,
                      profile_handlers, error_handlers)
import db


async def main():
    db.create_table()
    bot = Bot(token=os.getenv("BOT_TOKEN"), parse_mode="html")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(default_handlers.router, tutor_handlers.router, help_handlers.router,
                       command_handlers.router, alarm_handlers.router, profile_handlers.router, error_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except asyncio.exceptions.CancelledError:
        print("The polling cycle was interrupted")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
