from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
import db
import kb
from states import CommandStates

router = Router()


async def send_lost(msg: Message, lost_name, photo):
    await msg.answer_photo(photo, reply_markup=kb.join_command_kb(lost_name))


@router.message(F.text.lower() == "хочу помочь в поисках!")
async def help_message_handler(message: Message, state: FSMContext):
    await message.answer("Выберите, кому вы хотите и можете помочь", reply_markup=kb.back_kb())
    for args in db.get_all_lost_info():
        await send_lost(message, args[1], args[-1])
    await state.set_state(CommandStates.choosing)
    await state.update_data(id=message.from_user.id)


@router.message(CommandStates.choosing, F.text.lower() == "назад")
async def help_message_handler(message: Message, state: FSMContext):
    await message.answer("Выберите действие", reply_markup=kb.first_choose_kb())
    await state.clear()


@router.message(Command("chat"))
async def send_teammates(message: Message, command: CommandObject, bot: Bot):
    if command.args is None:
        return
    msg = db.get_human(message.from_user.id) + ": " + " ".join(command.args)
    for teammate in db.get_teammates(message.from_user.id):
        await bot.send_message(teammate, msg)


@router.callback_query(CommandStates.choosing)
async def join_team(callback: CallbackQuery, state: FSMContext):
    db.add_team_member((await state.get_data())["id"], callback.data)
    await callback.answer()
