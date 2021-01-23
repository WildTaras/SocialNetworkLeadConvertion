from aiogram.dispatcher.filters.state import StatesGroup, State


class RespondentState(StatesGroup):
    GetName = State()
    FirstQ = State()
    SecondQ = State()
    ThirdQ = State()
    FourthQ = State()
    FifthQ = State()
    SixthQ = State()
    SeventhQ = State()
