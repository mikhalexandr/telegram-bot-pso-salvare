from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji


class SelectionKeyboard:
    @staticmethod
    def select_action_kb():
        kb = [
            [KeyboardButton(text=emoji.emojize("🙏 Помогите найти!"))],
            [KeyboardButton(text=emoji.emojize("🔎 Хочу помочь в поисках!"))],
            [KeyboardButton(text=emoji.emojize("🆘 Мне срочно нужна помощь!"))],
            [KeyboardButton(text=emoji.emojize("👤 Профиль"))]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return keyboard
