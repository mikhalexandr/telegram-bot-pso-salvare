from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import emoji


class TeamKeyboard:
    @staticmethod
    def join_team_kb(lost_name):
        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton(text=emoji.emojize("👥 Присоединиться!"), callback_data=lost_name))
        return builder.as_markup()

    @staticmethod
    def leave_team_kb():
        kb = [
            [KeyboardButton(text="Покинуть команду")],
            [KeyboardButton(text=emoji.emojize("◀ Выйти"))]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return keyboard
