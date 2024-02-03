from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import AlarmStates
import consts
import db
import kb

router = Router()


@router.message(F.text.lower() == "мне срочно нужна помощь!")
async def geo_handler(message: Message, state: FSMContext):
    await message.answer("Сохраняйте спокойствие! Первым делом пришлите нам свою геопозицию!", reply_markup=kb.geo_kb())
    await state.set_state(AlarmStates.geodata)
    

@router.message(AlarmStates.geodata)
async def mobile_handler(message: Message, state: FSMContext):
    await state.update_data(geo=message.location)
    await message.answer("Отлично, мы получили геопозицию. Теперь пришлите Ваш номер телефона!",
                         reply_markup=kb.contact_kb())
    await state.set_state(AlarmStates.mobile)


@router.message(AlarmStates.mobile)
async def look_handler(message: Message, state: FSMContext):
    await state.update_data(mobile=message.contact)
    await message.answer("Опишите то, как вы сейчас выглядите: во что одеты, цвет волос, рост, телосложение",
                         reply_markup=kb.ReplyKeyboardRemove())
    await state.set_state(AlarmStates.look)


@router.message(AlarmStates.look, F.text)
async def situation_handler(message: Message, state: FSMContext):
    await state.update_data(look=message.text)
    await message.answer("Как вы попали в эту ситуацию? Что вас окружает?")
    await state.set_state(AlarmStates.situation)


@router.message(AlarmStates.situation, F.text)
async def note_handler(message: Message, state: FSMContext):
    await state.update_data(situation=message.text)
    await message.answer("Информация передана, скоро прибудет помощь! "
                         "Сохраняйте спокойствие, не уходите далеко от вашей нынешней геолокации "
                         "и соблюдайте меры предосторожности!")
    await state.set_state(AlarmStates.note)
