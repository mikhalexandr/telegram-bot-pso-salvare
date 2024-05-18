from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import db
import kb


router = Router()


@router.message(F.text.lower() == "профиль")
async def profile_message_handler(message: Message):
    await message.answer(f"Ваш id: {message.from_user.id}, ваше имя: {db.get_human(message.from_user.id)}",
                         reply_markup=kb.exit_kb())
