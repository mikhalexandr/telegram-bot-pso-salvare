from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import emoji


def first_choose_kb():
    kb = [[KeyboardButton(text=emoji.emojize("🙏 Помогите найти!"))],
          [KeyboardButton(text=emoji.emojize("🔎 Хочу помочь в поисках!"))],
          [KeyboardButton(text=emoji.emojize("🆘 Мне срочно нужна помощь!"))],
          [KeyboardButton(text=emoji.emojize("👤 Профиль"))]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def yes_or_no_kb():
    kb = [[KeyboardButton(text=emoji.emojize("✅ Да")), KeyboardButton(text=emoji.emojize("❌ Нет"))],
          [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def inline_finding_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=emoji.emojize("✅ В поиск!"), callback_data="letsfind"),
                InlineKeyboardButton(text=emoji.emojize("❌ Отклонить"), callback_data="reject"))
    return builder.as_markup()


def join_command_kb(lost_name):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=emoji.emojize("👥 Присоединиться!"), callback_data=lost_name))
    return builder.as_markup()


def geo_kb():
    kb = [[KeyboardButton(text=emoji.emojize("🌏 Отправить геопозицию"), request_location=True)],
          [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def contact_kb():
    kb = [[KeyboardButton(text=emoji.emojize("📞 Отправить контакт"), request_contact=True)],
          [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def inline_alarming_kb():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=emoji.emojize("✅ Помочь!"), callback_data="letsalarm"),
                InlineKeyboardButton(text=emoji.emojize("❌ Отклонить"), callback_data="alarmreject"))
    return builder.as_markup()


def skip_kb():
    kb = [[KeyboardButton(text=emoji.emojize("⏩ Пропустить"))], [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def leave_team_kb():
    kb = [[KeyboardButton(text="Покинуть команду")], [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def exit_kb():
    kb = [[KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def profile_kb():
    kb = [[KeyboardButton(text=emoji.emojize("♻ Изменить имя"))], [KeyboardButton(text=emoji.emojize("◀ Выйти"))]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def tutor_teams_control_kb(loser):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=emoji.emojize("🚫 Закрыть поиск"), callback_data=f"delteam_{loser}"),)
    return builder.as_markup()
