from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

async def poll_attendance(message: Message, bot: AsyncTeleBot):
    """ Starts a poll to collect attendance from group members.
    """
    await bot.send_message(message.chat.id, 
                           "Admin Sanity Check"
                           )