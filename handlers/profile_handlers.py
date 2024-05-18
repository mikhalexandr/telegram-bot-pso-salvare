from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import emoji

from states import LoadingNameStates
import db
import kb


router = Router()


@router.message(F.text.lower() == emoji.emojize("👤 профиль"))
async def profile_message_handler(message: Message, state: FSMContext):
    await message.answer(emoji.emojize(f"🆔 Ваш id: {message.from_user.id}\n"
                                       f"💬 Ваше имя: {db.get_human(message.from_user.id)}"),
                         reply_markup=kb.profile_kb())
    await state.set_state(LoadingNameStates.change_name)


@router.message(LoadingNameStates.change_name, F.text == "♻ Изменить имя")
async def change_name_handler(message: Message, state: FSMContext):
    await message.answer("Введите новое имя:", reply_markup=kb.exit_kb())
    await state.set_state(LoadingNameStates.change_ready)


@router.message(LoadingNameStates.change_ready, F.text)
async def change_ready_handler(message: Message, state: FSMContext):
    db.update_person_name(message.from_user.id, message.text)
    await message.answer(f"Ваше имя изменено на [{message.text}]")
    await message.answer(emoji.emojize(f"🆔 Ваш id: {message.from_user.id}\n"
                                       f"💬 Ваше имя: {db.get_human(message.from_user.id)}"),
                         reply_markup=kb.profile_kb())
    await state.clear()
