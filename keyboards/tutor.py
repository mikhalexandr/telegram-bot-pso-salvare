from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import emoji


class TutorKeyboard:
    @staticmethod
    def inline_alarming_kb():
        builder = InlineKeyboardBuilder()
        builder.row(
            InlineKeyboardButton(text=emoji.emojize("✅ Помочь!"), callback_data="letsalarm"),
            InlineKeyboardButton(text=emoji.emojize("❌ Отклонить"), callback_data="alarmreject")
        )
        return builder.as_markup()

    @staticmethod
    def inline_finding_kb(req_id):
        builder = InlineKeyboardBuilder()
        builder.row(
            InlineKeyboardButton(text=emoji.emojize("✅ В поиск!"), callback_data=f"letsfind:{req_id}"),
            InlineKeyboardButton(text=emoji.emojize("❌ Отклонить"), callback_data=f"reject:{req_id}")
        )
        return builder.as_markup()

    @staticmethod
    def tutor_teams_control_kb(lost):
        builder = InlineKeyboardBuilder()
        builder.row(
            InlineKeyboardButton(text=emoji.emojize("🚫 Закрыть поиск"), callback_data=f"delteam_{lost}")
        )
        return builder.as_markup()
