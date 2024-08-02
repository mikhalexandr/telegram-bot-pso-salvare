from aiogram.fsm.state import State, StatesGroup


class AlarmStates(StatesGroup):
    geodata = State()
    mobile = State()
    charge = State()
    name = State()
    look = State()
    situation = State()
    photo = State()
