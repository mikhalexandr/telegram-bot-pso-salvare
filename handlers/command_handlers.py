from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
import emoji

from states import CommandStates
import db
import kb

router = Router()


@router.message(F.text.lower() == emoji.emojize("🔎 хочу помочь в поисках!"))
async def help_message_handler(message: Message, state: FSMContext):
    if db.is_in_team(message.from_user.id):
        await message.answer("Выберите, кому вы хотите и можете помочь:", reply_markup=kb.leave_team_kb())
    else:
        await message.answer("Выберите, кому вы хотите и можете помочь:", reply_markup=kb.exit_kb())
    for args in db.get_all_lost_info():
        await message.answer_photo(args[-1], reply_markup=kb.join_command_kb(args[1]))
    await state.set_state(CommandStates.choosing)
    await state.update_data(id=message.from_user.id)


@router.message(CommandStates.choosing, F.text.lower() == "покинуть команду")
async def help_message_handler(message: Message):
    db.del_team_member(message.from_user.id)
    await message.answer("Успешно!", reply_markup=kb.exit_kb())


@router.message(Command("chat"))
async def send_teammates(message: Message, command: CommandObject, bot: Bot):
    if command.args is None:
        return
    msg = db.get_human(message.from_user.id) + ": " + command.args
    for teammate in db.get_teammates(message.from_user.id):
        if teammate[0]:
            await bot.send_message(teammate[0], msg)


@router.callback_query(CommandStates.choosing)
async def join_team(callback: CallbackQuery, state: FSMContext):
    id_ = (await state.get_data())["id"]
    db.update_comm_count(id_)
    db.del_team_member(id_)
    db.add_team_member(id_, callback.data)
    await callback.message.answer("Теперь вам доступна команда [/chat] для общения с товарищами по поиску!",
                                  reply_markup=kb.leave_team_kb())
    await callback.answer("Вы успешно присоединились к команде!")
