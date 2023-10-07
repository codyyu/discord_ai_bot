import asyncio
import logging

import discord
from config import Config
from discord.ext.commands import Bot

config = Config()

logging.basicConfig(level=logging.INFO)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
bot = Bot(command_prefix="?", intents=intents)


async def main() -> None:
    await bot.load_extension("cogs.onReady")
    await bot.load_extension("cogs.guildsDataUpdate")
    await bot.load_extension("cogs.msgDataUpdate")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
bot.run(token=config.DISCORD_BOT_TOKEN, root_logger=True, log_handler=None)
