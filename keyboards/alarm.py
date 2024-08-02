from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import emoji


class AlarmKeyboard:
    @staticmethod
    def geo_kb():
        kb = [[KeyboardButton(text=emoji.emojize("🌏 Отправить геопозицию"), request_location=True)],
              [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return keyboard

    @staticmethod
    def contact_kb():
        kb = [[KeyboardButton(text=emoji.emojize("📞 Отправить контакт"), request_contact=True)],
              [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return keyboard

    @staticmethod
    def skip_kb():
        kb = [[KeyboardButton(text=emoji.emojize("⏩ Пропустить"))], [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return keyboard
