from aiogram.fsm.state import State, StatesGroup


class TutorStates(StatesGroup):
    descript_reject = State()
    descript_accept = State()
    check_alarmik = State()
