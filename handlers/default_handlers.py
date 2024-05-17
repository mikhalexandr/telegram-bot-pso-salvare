from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states import LoadingNameStates
import consts


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await message.answer(consts.START_MESSAGE)
    await state.set_state(LoadingNameStates.load_name)


@router.message()
async def f(message: Message):
    await message.answer("Нет такого варианта!")
