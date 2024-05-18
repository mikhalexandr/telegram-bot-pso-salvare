from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import emoji
import os

from states import LoadInfoStates
from create_form import create_form
import db
import consts
import kb


router = Router()


@router.message(F.text.lower() == emoji.emojize("🙏 помогите найти!"))
async def help_message_handler(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, укажите полное имя пропавшего", reply_markup=kb.exit_kb())
    await state.set_state(LoadInfoStates.load_name)


@router.message(LoadInfoStates.load_name, F.text)
async def born_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите полную дату рождения пропавшего")
    await state.set_state(LoadInfoStates.load_born)


@router.message(LoadInfoStates.load_born, F.text)
async def regions_handler(message: Message, state: FSMContext):
    await state.update_data(born=message.text)
    await message.answer("Укажите регион, где произошла пропажа")
    await state.set_state(LoadInfoStates.load_region)


@router.message(LoadInfoStates.load_region, F.text)
async def description_handler(message: Message, state: FSMContext):
    await state.update_data(region=message.text)
    await message.answer("Укажите какую-либо информацию о произошедшем")
    await state.set_state(LoadInfoStates.load_description)


@router.message(LoadInfoStates.load_description, F.text)
async def feature_handler(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Укажите приметы пропавшего")
    await state.set_state(LoadInfoStates.load_feature)


@router.message(LoadInfoStates.load_feature, F.text)
async def spec_feature_handler(message: Message, state: FSMContext):
    await state.update_data(feature=message.text)
    await message.answer("Укажите особые приметы пропавшего")
    await state.set_state(LoadInfoStates.load_spec_feature)


@router.message(LoadInfoStates.load_spec_feature, F.text)
async def clothes_handler(message: Message, state: FSMContext):
    await state.update_data(spec_feature=message.text)
    await message.answer("Опишите, во что был одет пропавший")
    await state.set_state(LoadInfoStates.load_clothes)


@router.message(LoadInfoStates.load_clothes, F.text)
async def items_handler(message: Message, state: FSMContext):
    await state.update_data(clothes=message.text)
    await message.answer("Какие предметы были у пострадавшего при себе?")
    await state.set_state(LoadInfoStates.load_items)


@router.message(LoadInfoStates.load_items, F.text)
async def photo_handler(message: Message, state: FSMContext):
    await state.update_data(items=message.text)
    await message.answer("Пришлите фотографию пропавшего")
    await state.set_state(LoadInfoStates.load_photo)


@router.message(LoadInfoStates.load_photo, F.photo)
async def check_form_handler(message: Message, state: FSMContext):
    await message.bot.download(file=message.photo[-1].file_id, destination=f"photo{message.photo[-1].file_id}.jpg")
    await message.answer("Ваша заявка принята и выглядит так:")
    ll = await state.get_data()
    photo = create_form(*[ll[key] for key in ll], message.photo[-1].file_id)
    p = await message.answer_photo(photo)
    os.remove(f"image{message.photo[-1].file_id}.jpg")
    await state.update_data(photo=p.photo[-1].file_id)
    await message.answer("Всё верно?", reply_markup=kb.yes_or_no_kb())
    await state.set_state(LoadInfoStates.confirm)


@router.message(LoadInfoStates.confirm, F.text.lower() == emoji.emojize("✅ да"))
async def okay_handler(message: Message, state: FSMContext, bot: Bot):
    await message.answer("Отлично! Ваш запрос будет рассмотрен в ближайшее время!", reply_markup=kb.first_choose_kb())
    ll = await state.get_data()
    db.push_checking_info(message.from_user.id, *[ll[key] for key in ll])
    await bot.send_photo(consts.TUTOR_ID, ll["photo"], reply_markup=kb.inline_finding_kb())
    await state.clear()


@router.message(LoadInfoStates.confirm, F.text.lower() == emoji.emojize("❌ нет"))
async def repeat_handler(message: Message, state: FSMContext):
    await message.answer("Вы хотите заново заполнить анкету?", reply_markup=kb.yes_or_no_kb())
    await state.set_state(LoadInfoStates.confirm_restart)


@router.message(LoadInfoStates.confirm_restart, F.text.lower() == emoji.emojize("❌ нет"))
async def no_handler(message: Message, state: FSMContext):
    await message.answer("Выберите действие:", reply_markup=kb.first_choose_kb())
    await state.clear()


@router.message(LoadInfoStates.confirm_restart, F.text.lower() == emoji.emojize("✅ да"))
async def yes_handler(message: Message, state: FSMContext):
    await help_message_handler(message, state)
