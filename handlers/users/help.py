from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import Message

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: Message):
    pass
