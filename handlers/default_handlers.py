from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import consts
import kb
from states import LoadingNameStates
import db

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await message.answer(consts.START_MESSAGE)
    await state.set_state(LoadingNameStates.load_name)


@router.message(LoadingNameStates.load_name, F.text)
async def start_handler(message: Message, state: FSMContext):
    await message.answer(f"Здравствуйте, {message.text}! Выберите действие:", reply_markup=kb.first_choose_kb())
    db.add_human(message.from_user.id, message.text)
    await state.clear()


@router.message()
async def f(message: Message):
    await message.answer("Нет такого варианта!")
