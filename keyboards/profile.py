from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji


class ProfileKeyboard:
    @staticmethod
    def change_name_kb():
        kb = [
            [KeyboardButton(text=emoji.emojize("♻ Изменить имя"))],
            [KeyboardButton(text=emoji.emojize("◀ Выйти"))]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return keyboard
