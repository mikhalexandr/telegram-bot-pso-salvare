from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import TelegramConfig


class TutorFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == TelegramConfig.TUTOR_ID
