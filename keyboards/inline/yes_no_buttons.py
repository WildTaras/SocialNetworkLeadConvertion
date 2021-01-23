from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.choice_callback_data import ChoiceCallback

YesNo = InlineKeyboardMarkup(row_width=2,
                             inline_keyboard=
                             [
                                 [
                                     InlineKeyboardButton(
                                         text="Да,конечно",
                                         callback_data=ChoiceCallback.new(item_name="yes")
                                     ),
                                     InlineKeyboardButton(
                                         text="Нет, меня всё устраивает",
                                         callback_data=ChoiceCallback.new(item_name="no")
                                     )
                                 ]
                             ])

YesKeyboard = InlineKeyboardMarkup()

CHANNEL_LINK = "https://t.me/lvc_official"

channel_link = InlineKeyboardButton(text="Перейти!", url=CHANNEL_LINK)

YesKeyboard.insert(channel_link)