"""
Contains the main driver code for the Telegram Bot.
"""
# Library Imports.
import asyncio
from telebot.async_telebot import AsyncTeleBot

# File Imports.
import tgbot.config as config
from tgbot.handlers.non_group_message import non_group_message
from tgbot.handlers.help_message import help_message
from tgbot.handlers.poll_attendance import poll_attendance
from tgbot.filters.group_filter import GroupFilter
from tgbot.filters.group_admin_filter import GroupAdminfilter

bot = AsyncTeleBot(config.TOKEN)

# Register Message Handlers.
bot.register_message_handler(non_group_message, pass_bot=True, group=False)
bot.register_message_handler(help_message, commands=["start", "help"], pass_bot=True, group=True)
bot.register_message_handler(poll_attendance, commands=["poll"], pass_bot=True, group=True, group_admin=True)

# Register Message Filters.
bot.add_custom_filter(GroupFilter())
bot.add_custom_filter(GroupAdminfilter(bot))

if __name__ == "__main__":
    async def run():
        await bot.polling()

    print("Running Bot")
    asyncio.run(run())