from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await dp.bot.send_message(message.from_user.id, message.text)
