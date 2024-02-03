from aiogram.fsm.state import State, StatesGroup


class LoadingNameStates(StatesGroup):
    load_name = State()


class LoadInfoStates(StatesGroup):
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


class TutorStates(StatesGroup):
    descript_reject = State()
    descript_accept = State()


class AlarmStates(StatesGroup):
    geodata = State()
    mobile = State()
    name = State()
    look = State()
    situation = State()
    note = State()


class CommandStates(StatesGroup):
    choosing = State()

