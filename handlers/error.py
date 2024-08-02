from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def unknown(message: Message):
    await message.answer("Нет такого варианта!")
