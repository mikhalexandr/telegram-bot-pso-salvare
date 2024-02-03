from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import AlarmStates
import consts
import db
import kb

router = Router()


@router.message(F.text.lower() == "мне срочно нужна помощь!")
async def help_message_handler(message: Message, state: FSMContext):
    await message.answer("Сохраняйте спокойствие! Первым делом пришлите нам свою геопозицию!", reply_markup=kb.ReplyKeyboardRemove())
    await state.set_state(AlarmStates.geodata)
    

@router.message(AlarmStates.geodata, F.text)
async def born_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отлично, мы получили геопозицию. Теперь ввведите Ваш номер телефона!")
    await state.set_state(AlarmStates.mobile)


@router.message(AlarmStates.mobile, F.text)
async def regions_handler(message: Message, state: FSMContext):
    await state.update_data(born=message.text)
    await message.answer("Опишите то, как вы сейчас выглядите: во что одеты, цвет волос, рост, телосложение")
    await state.set_state(AlarmStates.look)


@router.message(AlarmStates.look, F.text)
async def regions_handler(message: Message, state: FSMContext):
    await state.update_data(born=message.text)
    await message.answer("Итак:")
    await state.set_state(AlarmStates.check)


@router.message(AlarmStates.check, F.text)
async def regions_handler(message: Message, state: FSMContext):
    await state.update_data(born=message.text)
    await message.answer("Информация передана, скоро прибудет помощь! "
                         "Сохраняйте спокойствие, не уходите далеко от вашей нынешней геолокации "
                         "и соблюдайте меры предосторожности!")
    await state.set_state(AlarmStates.note)
