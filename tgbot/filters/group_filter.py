from telebot.asyncio_filters import SimpleCustomFilter
from telebot.types import Message

class GroupFilter(SimpleCustomFilter):
    """ Defines a filter for checking if the message came from a chat group.
    """
    key = "group"

    async def check(self, message: Message):
        return message.chat.type == "group"