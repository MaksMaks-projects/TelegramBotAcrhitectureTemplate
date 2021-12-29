from aiogram.types import Message

from loader import dp


@dp.message_handler(state=None)
async def bot_echo(message: Message):
    pass
