from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
import consts

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(consts.START_MESSAGE)


@router.message()
async def f(message: Message):
    await message.answer("HELLO")
