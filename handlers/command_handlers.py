from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import os
import db
import consts
import kb

router = Router()


async def send_lost(msg: Message, lost_name, photo):
    await msg.answer_photo(photo, reply_markup=kb.join_command_kb(lost_name))


@router.message(F.text.lower() == "хочу помочь в поисках!")
async def help_message_handler(message: Message, state: FSMContext):
    await message.answer("Выберите, кому вы хотите и можете помочь", reply_markup=kb.ReplyKeyboardRemove())
    for args in db.get_all_lost_info():
        await send_lost(message, args[1], args[-1])
