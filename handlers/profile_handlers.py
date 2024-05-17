from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import db
import kb


router = Router()


@router.message(F.text.lower() == "выйти")
async def help_message_handler(message: Message, state: FSMContext):
    # current_state = await state.get_state()
    # if current_state is None:
    #     return
    # await state.clear()
    await message.answer("Выберите действие", reply_markup=kb.first_choose_kb())


@router.message(F.text.lower() == "профиль")
async def profile_message_handler(message: Message):
    await message.answer(f"Ваш id: {message.from_user.id}, ваше имя: {db.get_human(message.from_user.id)}",
                         reply_markup=kb.exit_kb())
