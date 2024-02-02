from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import consts
import kb
from states import LoadInfoStates
import db

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(consts.START_MESSAGE, reply_markup=kb.first_choose_kb())


@router.message(F.text.lower() == "помогите найти!")
async def help_message_handler(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, укажите полное имя пропавшего", reply_markup=kb.ReplyKeyboardRemove())
    await state.set_state(LoadInfoStates.load_name)


@router.message(LoadInfoStates.load_name, F.text)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите полную дату рождения пропавшего")
    await state.set_state(LoadInfoStates.load_born)


@router.message(LoadInfoStates.load_born, F.text)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(born=message.text)
    await message.answer("Укажите регион, где произошла пропажа")
    await state.set_state(LoadInfoStates.load_region)


@router.message(LoadInfoStates.load_region, F.text)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(region=message.text)
    await message.answer("Укажите какую-либо информацию о произошедшем")
    await state.set_state(LoadInfoStates.load_description)


@router.message(LoadInfoStates.load_description, F.text)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Укажите приметы пропавшего")
    await state.set_state(LoadInfoStates.load_feature)


@router.message(LoadInfoStates.load_feature, F.text)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(feature=message.text)
    await message.answer("Укажите особые приметы пропавшего")
    await state.set_state(LoadInfoStates.load_spec_feature)


@router.message(LoadInfoStates.load_spec_feature, F.text)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(spec_feature=message.text)
    await message.answer("Опишите, во что был одет пропавший")
    await state.set_state(LoadInfoStates.load_clothes)


@router.message(LoadInfoStates.load_clothes, F.text)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(clothes=message.text)
    await message.answer("Какие предметы были у пострадавшего при себе?")
    await state.set_state(LoadInfoStates.load_items)


@router.message(LoadInfoStates.load_items, F.text)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(items=message.text)
    await message.answer("Пришлите фотографию пропавшего")
    await state.set_state(LoadInfoStates.load_photo)


@router.message(LoadInfoStates.load_photo, F.photo)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Ваша заявка принята и выглядит так:")
    await message.answer("Всё верно?", reply_markup=kb.yes_or_no_kb())
    await state.set_state(LoadInfoStates.confirm)


@router.message(LoadInfoStates.confirm, F.text.lower() == "да")
async def name_handler(message: Message, state: FSMContext):
    await message.answer("Отлично! Мы найдем потерявшегося в ближайшее время!", reply_markup=kb.first_choose_kb())
    ll = await state.get_data()
    db.push_info(message.from_user.id, *[ll[key] for key in ll])
    await state.clear()


@router.message(LoadInfoStates.confirm, F.text.lower() == "нет")
async def name_handler(message: Message, state: FSMContext):
    await message.answer("Вы хотите заново заполнить анкету?", reply_markup=kb.yes_or_no_kb())
    await state.set_state(LoadInfoStates.confirm_restart)


@router.message(LoadInfoStates.confirm_restart, F.text.lower() == "нет")
async def name_handler(message: Message, state: FSMContext):
    await message.answer("Выберите действие", reply_markup=kb.first_choose_kb())
    await state.clear()


@router.message(LoadInfoStates.confirm_restart, F.text.lower() == "да")
async def name_handler(message: Message, state: FSMContext):
    await help_message_handler(message, state)


@router.message()
async def f(message: Message):
    await message.answer("Нет такого варианта!")
