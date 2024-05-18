from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
import emoji

from states import AlarmStates
import map
import consts
import db
import kb


router = Router()


@router.message(F.text.lower() == emoji.emojize("🆘 мне срочно нужна помощь!"))
async def geo_handler(message: Message, state: FSMContext):
    await message.answer("Сохраняйте спокойствие! Первым делом пришлите нам свою геопозицию!", reply_markup=kb.geo_kb())
    await state.set_state(AlarmStates.geodata)


@router.message(AlarmStates.geodata)
async def mobile_handler(message: Message, state: FSMContext):
    await state.update_data(geo=str(message.location.longitude) + "," + str(message.location.latitude))
    await message.answer("Отлично, мы получили геопозицию. Теперь пришлите Ваш номер телефона!",
                         reply_markup=kb.contact_kb())
    await state.set_state(AlarmStates.mobile)


@router.message(AlarmStates.mobile)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(mobile=message.contact.phone_number)
    await message.answer("Назовите свое имя, фамилию и отчество",
                         reply_markup=kb.exit_kb())
    await state.set_state(AlarmStates.name)


@router.message(AlarmStates.name, F.text)
async def charge_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Пожалуйста, впишите уровень заряда вашего устройства")
    await state.set_state(AlarmStates.charge)


@router.message(AlarmStates.charge, F.text)
async def look_handler(message: Message, state: FSMContext):
    await state.update_data(charge=message.text)
    await message.answer("Опишите то, как вы сейчас выглядите: во что одеты, цвет волос, рост, телосложение")
    await state.set_state(AlarmStates.look)


@router.message(AlarmStates.look, F.text)
async def situation_handler(message: Message, state: FSMContext):
    await state.update_data(look=message.text)
    await message.answer("Как вы попали в эту ситуацию? Что вас окружает?")
    await state.set_state(AlarmStates.situation)


@router.message(AlarmStates.situation, F.text)
async def photo_handler(message: Message, state: FSMContext):
    await state.update_data(situation=message.text)
    await message.answer(f"Пришлите свою фотографию или нажмите {emoji.emojize('⏩ Пропустить')},"
                         f" если у вас нет такой возможности",
                         reply_markup=kb.skip_kb())
    await state.set_state(AlarmStates.photo)


@router.message(AlarmStates.photo, F.text == emoji.emojize("⏩ Пропустить"))
async def note_handler_no_photo(message: Message, state: FSMContext, bot: Bot):
    ll = await state.get_data()
    db.add_alarmik(message.from_user.id, *[ll[key] for key in ll])
    db.add_alarm_id(message.from_user.id)
    await message.answer("Информация передана, скоро прибудет помощь! "
                         "Сохраняйте спокойствие, не уходите далеко от вашей нынешней геолокации "
                         "и соблюдайте меры предосторожности!", reply_markup=kb.first_choose_kb())
    await bot.send_message(consts.TUTOR_ID,
                           emoji.emojize(
                               f"<b>:collision:ВНИМАНИЕ!!! ЧЕЛОВЕК В ОПАСНОСТИ!!!:collision:</b>\nПоследняя геолокация:"
                               f"{ll['geo']}\n"
                               f"Номер телефона: {ll['mobile']}\nФИО: {ll['name']}\nУровень заряда аккумулятора: "
                               f"{ll['charge']}\n"
                               f"Описание человека: {ll['look']}\nОписание окружающей среды: {ll['situation']}"),
                           parse_mode=ParseMode.HTML, reply_markup=kb.inline_alarming_kb()
                           )
    await bot.send_photo(consts.TUTOR_ID, map.create_map(ll["geo"]))
    await state.clear()


@router.message(AlarmStates.photo, F.photo)
async def note_handler_photo(message: Message, state: FSMContext, bot: Bot):
    ll = await state.get_data()
    db.add_alarmik(message.from_user.id, *[ll[key] for key in ll], message.photo[-1].file_id)
    db.add_alarm_id(message.from_user.id)
    await message.answer("Информация передана, скоро прибудет помощь! "
                         "Сохраняйте спокойствие, не уходите далеко от вашей нынешней геолокации "
                         "и соблюдайте меры предосторожности!", reply_markup=kb.first_choose_kb())
    await bot.send_message(consts.TUTOR_ID,
                           emoji.emojize(
                               f"<b>:collision:ВНИМАНИЕ!!! ЧЕЛОВЕК В ОПАСНОСТИ!!!:collision:</b>\nПоследняя геолокация:"
                               f"{ll['geo']}\n"
                               f"Номер телефона: {ll['mobile']}\nФИО: {ll['name']}\nУровень заряда аккумулятора: "
                               f"{ll['charge']}\n"
                               f"Описание человека: {ll['look']}\nОписание окружающей среды: {ll['situation']}"),
                           parse_mode=ParseMode.HTML, reply_markup=kb.inline_alarming_kb()
                           )
    await bot.send_photo(consts.TUTOR_ID, map.create_map(ll["geo"]))
    await bot.send_photo(consts.TUTOR_ID, message.photo[-1].file_id)
    await state.clear()
