from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

StartButton = ReplyKeyboardMarkup(keyboard=
[
    [
        KeyboardButton(text="Начать")
    ]
],
    resize_keyboard=True,
    one_time_keyboard=True
)
