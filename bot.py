"""
Contains the main driver code for the Telegram Bot.
"""
# Library Imports.
import asyncio
from telebot.async_telebot import AsyncTeleBot

# File Imports.
import tgbot.config as config
from tgbot.handlers.help_message import help_message

bot = AsyncTeleBot(config.TOKEN)

# Register Message Handlers.
bot.register_message_handler(help_message, commands=["start", "help"], pass_bot=True)

if __name__ == "__main__":
    async def run():
        await bot.polling(non_stop=True)

    print("Running Bot")
    asyncio.run(run())