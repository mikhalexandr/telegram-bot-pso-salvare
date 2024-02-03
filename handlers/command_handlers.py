from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import os
import db
import consts
import kb

router = Router()


@router.message(F.text.lower() == "хочу помочь в поисках!")
async def help_message_handler(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, укажите полное имя пропавшего", reply_markup=kb.ReplyKeyboardRemove())
