from aiogram.filters import BaseFilter
from aiogram.types import Message

import consts


class TutorFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == consts.TUTOR_ID
