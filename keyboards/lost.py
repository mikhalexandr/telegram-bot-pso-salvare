from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji


class LostKeyboard:
    @staticmethod
    def yes_or_no_kb():
        kb = [
            [KeyboardButton(text=emoji.emojize("✅ Да")), KeyboardButton(text=emoji.emojize("❌ Нет"))],
            [KeyboardButton(text=emoji.emojize("◀ Выйти"))]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return keyboard
