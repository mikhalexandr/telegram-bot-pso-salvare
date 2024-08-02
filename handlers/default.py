from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import emoji

from keyboards import SelectionKeyboard
from data import Users
from config import TelegramTexts
from states import ProfileStates


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    if Users.check_user_id(message.from_user.id) == 1:
        await message.answer(emoji.emojize(f"👋 Здравствуйте, {Users.get_user(message.from_user.id)}! "
                                           f"Выберите действие:"),
                             reply_markup=SelectionKeyboard.select_action_kb())
        await state.clear()
    else:
        await message.answer(TelegramTexts.START_MESSAGE)
        await state.set_state(ProfileStates.load_name)


@router.message(ProfileStates.load_name, F.text)
async def start_handler(message: Message, state: FSMContext):
    await message.answer(emoji.emojize(f"👋 Здравствуйте, {message.text}! Выберите действие:"),
                         reply_markup=SelectionKeyboard.select_action_kb())
    Users.add_user(message.from_user.id, message.text)
    await state.clear()


@router.message(F.text.lower() == emoji.emojize("◀ выйти"))
async def help_message_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=SelectionKeyboard.select_action_kb())


@router.message(Command("form_template"))
async def form_template_handler(message: Message):
    await message.answer_photo(photo=FSInputFile(path="data/form-template.png"),
                               caption="Шаблон анкеты о пострадавшем")
