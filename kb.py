from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def first_choose_kb():
    kb = [[KeyboardButton(text="Помогите найти!")], [KeyboardButton(text="Хочу помочь в поисках!")],
          [KeyboardButton(text="Мне срочно нужна помощь!")], [KeyboardButton(text="Профиль")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def yes_or_no_kb():
    kb = [[KeyboardButton(text="Да"), KeyboardButton(text="Нет")], [KeyboardButton(text="Выйти")]]
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


def geo_kb():
    kb = [[KeyboardButton(text="Отправить геопозицию", request_location=True)], [KeyboardButton(text="Выйти")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def contact_kb():
    kb = [[KeyboardButton(text="Отправить контакт", request_contact=True)], [KeyboardButton(text="Выйти")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def inline_alarming_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Помочь!", callback_data="letsalarm"),
                InlineKeyboardButton(text="Отклонить", callback_data="alarmreject"))
    return builder.as_markup()


def skip_kb():
    kb = [[KeyboardButton(text="Пропустить")], [KeyboardButton(text="Выйти")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def leave_team_kb():
    kb = [[KeyboardButton(text="Покинуть команду")], [KeyboardButton(text="Выйти")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def exit_kb():
    kb = [[KeyboardButton(text="Выйти")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def tutor_teams_control_kb(loser):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Закрыть поиск", callback_data=f"delteam_{loser}"),)
    return builder.as_markup()
