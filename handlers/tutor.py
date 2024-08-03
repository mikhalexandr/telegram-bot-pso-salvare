import os
from aiogram import Router, F, Bot, exceptions
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
import emoji

from keyboards import TutorKeyboard
from data import Lost, Teams, Checking, Users, Alarm
from config import TelegramConfig
from states import TutorStates
from filters import TutorFilter
from misc import request_image, create_map


router = Router()
router.message.filter(TutorFilter())


@router.message(Command("teams"))
async def teams_control(msg: Message):
    for args in Lost.get_all_lost():
        await msg.answer_photo(args[-1], reply_markup=TutorKeyboard.tutor_teams_control_kb(args[1]))


@router.callback_query(F.data.startswith("delteam_"))
async def delete_team(callback: CallbackQuery):
    loser = callback.data.replace("delteam_", "")
    Teams.delete_team(loser)
    Lost.delete_lost(loser)
    await callback.message.delete()
    await callback.answer(f"Поиск {loser} успешно закрыт!")


@router.callback_query(F.data.startswith("letsfind:"))
async def accept_lost_fin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    info = Checking.get_checking(callback.data.split(":")[1])
    await state.set_state(TutorStates.descript_accept)
    await state.update_data(user_id=info[0], photo=info[-1], loser_name=info[1])
    Checking.delete_checking(info[1])
    Lost.add_lost(*info)
    await bot.send_message(TelegramConfig.TUTOR_ID, "Введите полную информацию про поиск:")
    await callback.answer()


@router.callback_query(F.data.startswith("reject:"))
async def reject_lost_fin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    info = Checking.get_checking(callback.data.split(":")[1])
    await state.set_state(TutorStates.descript_reject)
    await state.update_data(user_id=info[0])
    Checking.delete_checking(info[1])
    await bot.send_message(TelegramConfig.TUTOR_ID, "Укажите причину отклонения запроса:")
    await callback.answer()


@router.message(TutorStates.descript_reject, F.text)
async def send_lost_reject_msg(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message((await state.get_data())["user_id"], f"Ваш поиск отклонен!\n{message.text}")
    await state.clear()


@router.message(TutorStates.descript_accept, F.text)
async def send_lost_accept_msg(message: Message, state: FSMContext, bot: Bot):
    Users.update_lost_count((await state.get_data())["user_id"])
    await bot.send_message((await state.get_data())["user_id"], "Ваш поиск принят!")
    ll = await state.get_data()
    Teams.create_team(ll["loser_name"])
    for user in Users.get_users():
        await bot.send_photo(user, ll["photo"], caption=message.text)
    await state.clear()


@router.callback_query(F.data.startswith("letsalarm:"))
async def accept_alarm_fin(callback: CallbackQuery, bot: Bot):
    user_geo = callback.data.split(":")[1]
    user_name = callback.data.split(":")[2]
    ll = Alarm.get_alarm(user_geo, user_name)
    photo = ll[-1]
    p = None
    try:
        if photo == "no_photo":
            request_image(ll[5])
            p = await bot.send_photo(TelegramConfig.TUTOR_ID, FSInputFile("assets/temporary/generated.jpg"),
                                     caption="Сгенерированное изображение")
        for user in Users.get_users():
            await bot.send_message(user, emoji.emojize(
                f"<b>:collision:ВНИМАНИЕ!!! ЧЕЛОВЕК В ОПАСНОСТИ!!!:collision:</b>\nПоследняя геолокация: "
                f"{ll[1].split(',')[0]}, {ll[1].split(',')[1]}\n"
                f"Номер телефона: {ll[2]}\nФИО: {ll[3]}\nУровень заряда аккумулятора: "
                f"{ll[4]}\n"
                f"Описание человека: {ll[5]}\nОписание окружающей среды: {ll[6]}"),
                                   parse_mode=ParseMode.HTML)
            await bot.send_photo(user, create_map(ll[1]))
            if photo != "no_photo":
                await bot.send_photo(user, photo,
                                     caption="Фотография пострадавшего")
            else:
                await bot.send_photo(user, p.photo[-1].file_id,
                                     caption="Изображение пострадавшего, сгенерированное нейросетью")
        if photo == "no_photo":
            os.remove("assets/temporary/generated.jpg")
        await callback.answer("Рассылка отправлена")
    except exceptions.TelegramBadRequest:
        print("OK")


@router.callback_query(F.data.startswith("alarmreject:"))
async def reject_alarm_fin(callback: CallbackQuery):
    user_geo = callback.data.split(":")[1]
    user_name = callback.data.split(":")[2]
    Alarm.delete_alarm(user_geo, user_name)
    await callback.answer("Запрос успешно отклонен!")
