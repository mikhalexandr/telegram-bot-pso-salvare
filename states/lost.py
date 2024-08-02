from aiogram.fsm.state import State, StatesGroup


class LostStates(StatesGroup):
    load_name = State()
    load_born = State()
    load_region = State()
    load_description = State()
    load_feature = State()
    load_spec_feature = State()
    load_clothes = State()
    load_items = State()
    load_photo = State()
    confirm = State()
    confirm_restart = State()
