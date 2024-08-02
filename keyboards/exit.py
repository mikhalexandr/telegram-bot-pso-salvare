from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji


class ExitKeyboard:
    @staticmethod
    def exit_kb():
        kb = [
            [KeyboardButton(text=emoji.emojize("◀ Выйти"))]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return keyboard
