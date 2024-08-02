from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
import emoji

from keyboards import TeamKeyboard, ExitKeyboard
from data import Teams, Lost, Users
from states import TeamStates


router = Router()


@router.message(F.text.lower() == emoji.emojize("🔎 хочу помочь в поисках!"))
async def help_message_handler(message: Message, state: FSMContext):
    if Teams.is_in_team(message.from_user.id):
        await message.answer("Выберите, кому вы хотите и можете помочь:", reply_markup=TeamKeyboard.leave_team_kb())
    else:
        await message.answer("Выберите, кому вы хотите и можете помочь:", reply_markup=ExitKeyboard.exit_kb())
    for args in Lost.get_all_lost():
        await message.answer_photo(args[-1], reply_markup=TeamKeyboard.join_team_kb(args[1]))
    await state.set_state(TeamStates.choosing)
    await state.update_data(id=message.from_user.id)


@router.message(TeamStates.choosing, F.text.lower() == "покинуть команду")
async def leave_team(message: Message):
    Teams.delete_teammate(message.from_user.id)
    await message.answer("Успешно!", reply_markup=ExitKeyboard.exit_kb())


@router.message(Command("chat"))
async def send_teammates(message: Message, command: CommandObject, bot: Bot):
    if command.args is None:
        return
    msg = Users.get_user(message.from_user.id) + ": " + command.args
    for teammate in Teams.get_teammates(message.from_user.id):
        if teammate[0]:
            await bot.send_message(teammate[0], msg)


@router.callback_query(TeamStates.choosing)
async def join_team(callback: CallbackQuery, state: FSMContext):
    id_ = (await state.get_data())["id"]
    Users.update_team_count(id_)
    Teams.delete_teammate(id_)
    Teams.add_teammate(id_, callback.data)
    await callback.message.answer("Теперь вам доступна команда [/chat] для общения с товарищами по поиску!",
                                  reply_markup=TeamKeyboard.leave_team_kb())
    await callback.answer("Вы успешно присоединились к команде!")
