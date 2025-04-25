from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

async def help_message(message: Message, bot: AsyncTeleBot):
    """ Sends a help message detailing the intended usage of the bot with a list
        of available commands.
    """
    await bot.send_message(message.chat.id, "Hello")