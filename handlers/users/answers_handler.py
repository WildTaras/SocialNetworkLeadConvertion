from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.default import FirstQuestionButtons
from keyboards.default.buttons_for_answers import SecondQuestionButtons, ThirdQuestionButtons, thirdQuestionButton3
from keyboards.default.start_button import StartButton
from keyboards.inline.choice_callback_data import ChoiceCallback
from keyboards.inline.yes_no_buttons import YesNo, YesKeyboard
from loader import dp, bot
from state.respondent_states import RespondentState


@dp.message_handler(Command("start"))
async def enter_test(message: types.Message):
    await message.answer("Рада тебя приветствовать в моём боте.\n"
                         "Спасибо тебе за интерес, мне очень приятно.\n"
                         "Я хочу узнать твои намерения\n"
                         "Отвечай, пожалуйста честно\n",
                         reply_markup=StartButton)


@dp.message_handler(text="Начать")
async def enter_start_button(message: types.Message):
    await message.answer("В первую очередь, мне бы хотелось узнать \n"
                         "как тебя зовут?")
    await RespondentState.GetName.set()


@dp.message_handler(state=RespondentState.GetName)
async def get_name_ask_first(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(respondent_name=name)
    await message.answer(f"{name}, укажи пожалуйста, какой твой возраст?",
                         reply_markup=FirstQuestionButtons)
    await RespondentState.FirstQ.set()


@dp.message_handler(state=RespondentState.FirstQ)
async def get_first_ask_second(message: types.Message, state: FSMContext):
    await message.answer("Скажи пожалуйста, какой из нижеперечисленных\n"
                         "форматов для тебя более подходящий?",
                         reply_markup=SecondQuestionButtons)
    # Нужно будет хранить это значение где-то, чтобы понять какого возраста
    # чуваки ведутся на конкретную девочку

    await RespondentState.SecondQ.set()


@dp.message_handler(state=RespondentState.SecondQ)
async def get_second_ask_third(message: types.Message, state: FSMContext):
    await message.answer("Часто ли ты ходишь на свидания?",
                         reply_markup=ThirdQuestionButtons)
    await RespondentState.ThirdQ.set()


@dp.message_handler(state=RespondentState.ThirdQ)
async def get_third_ask_fourth(message: types.Message, state: FSMContext):
    if message.text == thirdQuestionButton3:
        await message.answer("Хочешь что-то изменить в этой жизни?",
                             reply_markup=YesNo)


@dp.callback_query_handler(ChoiceCallback.filter(item_name="yes"), state=RespondentState.ThirdQ)
async def choice_answer(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("я хочу тебя пригласить на свой авторский канал \n"
                              "где ты узнаешь, как начать регулярно ходить на свидания.",
                              reply_markup=YesKeyboard)


@dp.callback_query_handler(ChoiceCallback.filter(item_name="no"), state=RespondentState.ThirdQ)
async def choice_answer(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await RespondentState.FifthQ.set()
