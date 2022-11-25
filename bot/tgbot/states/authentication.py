from aiogram.dispatcher.filters.state import State, StatesGroup


class AuthenticationState(StatesGroup):
    waiting_for_email = State()
    waiting_for_name = State()
    waiting_for_surname = State()
    waiting_for_patronymic = State()
    waiting_for_group_name = State()
    waiting_for_confirmation = State()
