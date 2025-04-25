from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

async def non_group_message(message: Message, bot: AsyncTeleBot):
    """ Replies to messages in private chats informing users to use the bot in a group.
    """
    await bot.send_message(message.chat.id, 
                           "Hello! I am meant to be used in a group chat. Please add me to a group to proceed."
                           )