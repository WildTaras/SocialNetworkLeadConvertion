from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

firstQuestionButton1 = "18 - 25"
firstQuestionButton2 = "25 - 30"
firstQuestionButton3 = " >30 "
firstQuestionButton4 = "None"

FirstQuestionButtons = ReplyKeyboardMarkup(keyboard=
[
    [
        KeyboardButton(text=firstQuestionButton1),
        KeyboardButton(text=firstQuestionButton2),
        KeyboardButton(text=firstQuestionButton3)
    ]
],
    resize_keyboard=True,
    one_time_keyboard=True
)

secondQuestionButton1 = "Просто общение"
secondQuestionButton2 = "Просто секс"
secondQuestionButton3 = "Свободные отношения"
secondQuestionButton4 = "Серьезные отношения"
SecondQuestionButtons = ReplyKeyboardMarkup(keyboard=
[
    [
        KeyboardButton(text=secondQuestionButton1),
        KeyboardButton(text=secondQuestionButton2)
    ],
    [
        KeyboardButton(text=secondQuestionButton3),
        KeyboardButton(text=secondQuestionButton4)
    ]
],
    resize_keyboard=True,
    one_time_keyboard=True)

thirdQuestionButton1 = "Пока не хожу на свидания"
thirdQuestionButton2 = "Меньше 5 раз в месяц"
thirdQuestionButton3 = "5 - 10 раз в месяц"
thirdQuestionButton4 = "Больше 10 раз в месяц"
ThirdQuestionButtons = ReplyKeyboardMarkup(keyboard=
[
    [
        KeyboardButton(text=thirdQuestionButton1),
        KeyboardButton(text=thirdQuestionButton2)
    ],
    [
        KeyboardButton(text=thirdQuestionButton3),
        KeyboardButton(text=thirdQuestionButton4)
    ]
],
    resize_keyboard=True,
    one_time_keyboard=True)
