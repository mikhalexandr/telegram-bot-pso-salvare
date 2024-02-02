from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def first_choose_kb():
    kb = [[KeyboardButton(text="Помогите найти!")], [KeyboardButton(text="Хочу помочь в поисках!")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard
