from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(CommandStart())
async def start_bot(message: types.Message):
    '''Обработка команды /start'''
    pass