from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import consts
import kb

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(consts.START_MESSAGE, reply_markup=kb.first_choose_kb())


@router.message()
async def f(message: Message):
    await message.answer("HELLO", reply_markup=kb.ReplyKeyboardRemove())
