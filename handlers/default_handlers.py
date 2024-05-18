from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import emoji

from states import LoadingNameStates
import consts
import db
import kb


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    if db.check_id(message.from_user.id) == 1:
        await message.answer(emoji.emojize(f"👋 Здравствуйте, {db.get_human(message.from_user.id)}! Выберите действие:"),
                             reply_markup=kb.first_choose_kb())
        await state.clear()
    else:
        await message.answer(consts.START_MESSAGE)
        await state.set_state(LoadingNameStates.load_name)


@router.message(LoadingNameStates.load_name, F.text)
async def start_handler(message: Message, state: FSMContext):
    await message.answer(emoji.emojize(f"👋 Здравствуйте, {message.text}! Выберите действие:"),
                         reply_markup=kb.first_choose_kb())
    db.add_human(message.from_user.id, message.text)
    await state.clear()


@router.message(F.text.lower() == emoji.emojize("◀ выйти"))
async def help_message_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Выберите действие:", reply_markup=kb.first_choose_kb())


@router.message(Command("form_template"))
async def form_template_handler(message: Message):
    await message.answer_photo(photo=FSInputFile(path="data/form-template.png"),
                               caption="Шаблон анкеты о пострадавшем")
