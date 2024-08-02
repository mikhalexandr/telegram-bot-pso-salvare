from aiogram.fsm.state import State, StatesGroup


class TeamStates(StatesGroup):
    choosing = State()
