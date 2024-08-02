from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import emoji

from keyboards import ProfileKeyboard, ExitKeyboard
from data import Users
from config import TelegramConfig
from states import ProfileStates


router = Router()


@router.message(F.text.lower() == emoji.emojize("👤 профиль"))
async def profile_message_handler(message: Message, state: FSMContext):
    info = Users.get_user_info(message.from_user.id)
    lost_count, team_count, alarm_count = info[0], info[1], info[2]
    await message.answer(emoji.emojize(
        f"🆔 Ваш id: {message.from_user.id}\n"
        f"💬 Ваше имя: {Users.get_user(message.from_user.id)}\n"
        f"🎭 Ваша роль: "
        f"{'Администратор' if message.from_user.id == TelegramConfig.TUTOR_ID else 'Пользователь'}\n"
        f"🙏 Количество одобренных анкет: {lost_count}\n"
        f"👥 Количество участий в поисках: {team_count}\n"
        f"🆘 Количество одобренных обращений: {alarm_count}"),
        reply_markup=ProfileKeyboard.change_name_kb()
    )
    await state.set_state(ProfileStates.change_name)


@router.message(ProfileStates.change_name, F.text == "♻ Изменить имя")
async def change_name_handler(message: Message, state: FSMContext):
    await message.answer("Введите новое имя:", reply_markup=ExitKeyboard.exit_kb())
    await state.set_state(ProfileStates.change_ready)


@router.message(ProfileStates.change_ready, F.text)
async def change_ready_handler(message: Message, state: FSMContext):
    Users.update_user_name(message.from_user.id, message.text)
    await message.answer(f"Ваше имя изменено на [{message.text}]")
    info = Users.get_user_info(message.from_user.id)
    lost_count, team_count, alarm_count = info[0], info[1], info[2]
    await message.answer(emoji.emojize(
        f"🆔 Ваш id: {message.from_user.id}\n"
        f"💬 Ваше имя: {Users.get_user(message.from_user.id)}\n"
        f"🎭 Ваша роль: "
        f"{'Администратор' if message.from_user.id == TelegramConfig.TUTOR_ID else 'Пользователь'}\n"
        f"🙏 Количество одобренных анкет: {lost_count}\n"
        f"👥 Количество участий в поисках: {team_count}\n"
        f"🆘 Количество одобренных обращений: {alarm_count}"),
        reply_markup=ProfileKeyboard.change_name_kb()
    )
    await state.clear()
