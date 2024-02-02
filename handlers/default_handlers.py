from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def f(message: Message):
    await message.answer("HELLO")
