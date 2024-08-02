from aiogram.fsm.state import State, StatesGroup


class ProfileStates(StatesGroup):
    load_name = State()
    change_name = State()
    change_ready = State()
