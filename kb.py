from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def first_choose_kb():
    kb = [[KeyboardButton(text="Помогите найти!")], [KeyboardButton(text="Хочу помочь в поисках!")],
          [KeyboardButton(text="Мне срочно нужна помощь!")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def yes_or_no_kb():
    kb = [[KeyboardButton(text="Да"), KeyboardButton(text="Нет")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def inline_finding_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="В поиск!", callback_data="letsfind"),
                InlineKeyboardButton(text="Отклонить", callback_data="reject"))
    return builder.as_markup()


def join_command_kb(lost_name):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Присоединиться!", callback_data=lost_name))
    return builder.as_markup()


def back_kb():
    kb = [[KeyboardButton(text="Назад")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard