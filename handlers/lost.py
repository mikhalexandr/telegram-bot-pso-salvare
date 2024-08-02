import os
from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import emoji

from keyboards import LostKeyboard, ExitKeyboard, SelectionKeyboard, TutorKeyboard
from data import Checking
from config import TelegramConfig
from states import LostStates
from misc import create_form


router = Router()


@router.message(F.text.lower() == emoji.emojize("🙏 помогите найти!"))
async def help_message_handler(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, укажите полное имя пропавшего", reply_markup=ExitKeyboard.exit_kb())
    await state.set_state(LostStates.load_name)


@router.message(LostStates.load_name, F.text)
async def born_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите полную дату рождения пропавшего")
    await state.set_state(LostStates.load_born)


@router.message(LostStates.load_born, F.text)
async def regions_handler(message: Message, state: FSMContext):
    await state.update_data(born=message.text)
    await message.answer("Укажите регион, где произошла пропажа")
    await state.set_state(LostStates.load_region)


@router.message(LostStates.load_region, F.text)
async def description_handler(message: Message, state: FSMContext):
    await state.update_data(region=message.text)
    await message.answer("Укажите какую-либо информацию о произошедшем")
    await state.set_state(LostStates.load_description)


@router.message(LostStates.load_description, F.text)
async def feature_handler(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Укажите приметы пропавшего")
    await state.set_state(LostStates.load_feature)


@router.message(LostStates.load_feature, F.text)
async def spec_feature_handler(message: Message, state: FSMContext):
    await state.update_data(feature=message.text)
    await message.answer("Укажите особые приметы пропавшего")
    await state.set_state(LostStates.load_spec_feature)


@router.message(LostStates.load_spec_feature, F.text)
async def clothes_handler(message: Message, state: FSMContext):
    await state.update_data(spec_feature=message.text)
    await message.answer("Опишите, во что был одет пропавший")
    await state.set_state(LostStates.load_clothes)


@router.message(LostStates.load_clothes, F.text)
async def items_handler(message: Message, state: FSMContext):
    await state.update_data(clothes=message.text)
    await message.answer("Какие предметы были у пострадавшего при себе?")
    await state.set_state(LostStates.load_items)


@router.message(LostStates.load_items, F.text)
async def photo_handler(message: Message, state: FSMContext):
    await state.update_data(items=message.text)
    await message.answer("Пришлите фотографию пропавшего")
    await state.set_state(LostStates.load_photo)


@router.message(LostStates.load_photo, F.photo)
async def check_form_handler(message: Message, state: FSMContext):
    await message.bot.download(file=message.photo[-1].file_id,
                               destination=f"assets/temporary/photo{message.photo[-1].file_id}.jpg")
    await message.answer("Ваша заявка принята и выглядит так:")
    ll = await state.get_data()
    photo = create_form(*[ll[key] for key in ll], message.photo[-1].file_id)
    p = await message.answer_photo(photo)
    os.remove(f"assets/temporary/image{message.photo[-1].file_id}.jpg")
    await state.update_data(photo=p.photo[-1].file_id)
    await message.answer("Всё верно?", reply_markup=LostKeyboard.yes_or_no_kb())
    await state.set_state(LostStates.confirm)


@router.message(LostStates.confirm, F.text.lower() == emoji.emojize("✅ да"))
async def okay_handler(message: Message, state: FSMContext, bot: Bot):
    await message.answer("Отлично! Ваш запрос будет рассмотрен в ближайшее время!",
                         reply_markup=SelectionKeyboard.select_action_kb())
    ll = await state.get_data()
    Checking.add_checking(message.from_user.id, *[ll[key] for key in ll])
    await bot.send_photo(TelegramConfig.TUTOR_ID, ll["photo"], reply_markup=TutorKeyboard.inline_finding_kb())
    await state.clear()


@router.message(LostStates.confirm, F.text.lower() == emoji.emojize("❌ нет"))
async def repeat_handler(message: Message, state: FSMContext):
    await message.answer("Вы хотите заново заполнить анкету?", reply_markup=LostKeyboard.yes_or_no_kb())
    await state.set_state(LostStates.confirm_restart)


@router.message(LostStates.confirm_restart, F.text.lower() == emoji.emojize("❌ нет"))
async def no_handler(message: Message, state: FSMContext):
    await message.answer("Выберите действие:", reply_markup=SelectionKeyboard.select_action_kb())
    await state.clear()


@router.message(LostStates.confirm_restart, F.text.lower() == emoji.emojize("✅ да"))
async def yes_handler(message: Message, state: FSMContext):
    await help_message_handler(message, state)
