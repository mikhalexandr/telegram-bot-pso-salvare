import os

from aiogram import Router, F, Bot
import emoji
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from states import TutorStates
import consts
import map
import db
from filters import TutorFilter
import generate_by_request

router = Router()
router.message.filter(TutorFilter())


@router.callback_query(F.data == "letsfind")
async def accept_fin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    info = db.get_checking_info()
    await state.set_state(TutorStates.descript_accept)
    await state.update_data(user_id=info[0], photo=info[-1], loser_name=info[1])
    db.delete_checking(info[1])
    db.push_lost_info(*info)
    await bot.send_message(consts.TUTOR_ID, "Введите полную информацию про поиск:")
    await callback.answer()


@router.callback_query(F.data == "reject")
async def reject_fin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    info = db.get_checking_info()
    await state.set_state(TutorStates.descript_reject)
    await state.update_data(user_id=info[0])
    db.delete_checking(info[1])
    await bot.send_message(consts.TUTOR_ID, "Укажите причину отклонения запроса:")
    await callback.answer()


@router.message(TutorStates.descript_reject, F.text)
async def send_reject_msg(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message((await state.get_data())["user_id"], f"Ваш поиск отклонен!\n{message.text}")
    await state.clear()


@router.message(TutorStates.descript_accept, F.text)
async def send_accept_msg(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message((await state.get_data())["user_id"], f"Ваш поиск принят!")
    ll = await state.get_data()
    db.create_team(ll["loser_name"])
    for user in db.get_all():
        await bot.send_photo(user, ll["photo"], caption=message.text)
    await state.clear()


@router.callback_query(F.data == "letsalarm")
async def accept_fin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    ll = db.get_alarmik()
    generate_by_request.generate(ll[4])
    p = await bot.send_photo(consts.TUTOR_ID, FSInputFile("generated.jpg"))
    await p.delete()
    for user in db.get_all():
        await bot.send_message(user, emoji.emojize(
            f"<b>:collision:ВНИМАНИЕ!!! ЧЕЛОВЕК В ОПАСНОСТИ!!!:collision:</b>\nПоследняя геолокация:"
            f"{ll[0]}\n"
            f"Номер телефона: {ll[1]}\nФИО: {ll[2]}\nУровень заряда аккумулятора: "
            f"{ll[3]}\n"
            f"Был одет: {ll[4]}\nОписание человеком окружающей среды: {ll[5]}"),
                               parse_mode=ParseMode.HTML)
        await bot.send_photo(user, map.create_map(ll[0]))
        await bot.send_photo(user, p.photo[-1].file_id, caption="Изображение пострадавшего, сгенерированное нейросетью")
    await callback.answer()
