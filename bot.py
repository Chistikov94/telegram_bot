from aiogram import executor

import handlers
from loader import dp

async def on_startup(dp):
    '''Действия во время запуска бота'''
    pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)