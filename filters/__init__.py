from aiogram import Dispatcher

def setup(dp: Dispatcher):
    dp.filters_factory.bind()