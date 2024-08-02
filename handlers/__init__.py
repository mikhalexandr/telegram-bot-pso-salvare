from aiogram import Dispatcher

from .alarm import router as alarm_router
from .team import router as command_router
from .default import router as default_router
from .error import router as error_router
from .lost import router as help_router
from .profile import router as profile_router
from .tutor import router as tutor_router


def include_routers(dp: Dispatcher):
    dp.include_routers(default_router, help_router, tutor_router, alarm_router, command_router,
                      profile_router, error_router)
