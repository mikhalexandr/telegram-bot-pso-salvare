from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import TutorStates
import consts
import db
from filters import TutorFilter

router = Router()
router.message.filter(TutorFilter())


@router.callback_query(F.data == "letsfind")
async def accept_fin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    info = db.get_checking_info()
    await state.set_state(TutorStates.descript_accept)
    await state.update_data(user_id=info[0])
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
    for user in db.get_all():
        await bot.send_photo(consts.TUTOR_ID, ll["photo"])
    await state.clear()
