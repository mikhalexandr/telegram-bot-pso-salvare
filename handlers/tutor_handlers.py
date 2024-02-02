from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import kb
from states import LoadInfoStates
import db
from filters import TutorFilter

router = Router()
router.message.filter(TutorFilter())


@router.callback_query(F.data == "letsfind")
async def accept_fin(callback: CallbackQuery, bot: Bot):
    info = db.get_checking_info()
    await bot.send_message(info[0], "Ваш поиск одобрен!")
    db.delete_checking(info[1])
    db.push_lost_info(*info)
    await callback.answer()


@router.callback_query(F.data == "reject")
async def reject_fin(callback: CallbackQuery, bot: Bot):
    info = db.get_checking_info()
    await bot.send_message(info[0], "К сожалению, ваш поиск отклонен!")
    db.delete_checking(info[1])
    await callback.answer()
