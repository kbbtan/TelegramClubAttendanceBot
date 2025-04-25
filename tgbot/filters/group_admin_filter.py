from telebot.asyncio_filters import SimpleCustomFilter
from telebot.types import Message
from telebot.async_telebot import AsyncTeleBot

class GroupAdminfilter(SimpleCustomFilter):
    """ Defines a filter for checking if the message came from a chat group admin.
    """
    key = "group_admin"

    def __init__(self, bot: AsyncTeleBot):
        self.bot = bot

    async def check(self, message: Message):
        admins = await self.bot.get_chat_administrators(message.chat.id)
        admin_ids = [admin.user.id for admin in admins]

        return message.from_user.id in admin_ids