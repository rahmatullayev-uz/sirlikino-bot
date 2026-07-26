from aiogram.fsm.state import State, StatesGroup


class manage_movie_state(StatesGroup):
    get_file = State()
    get_name = State()