import asyncio
import logging

import discord
from config import Config
from discord import Message
from discord.ext.commands import Bot

config = Config()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)
handler.setLevel(logging.INFO)

bot = Bot(command_prefix="?", intents=intents)


@bot.event
async def on_ready() -> None:
    logger.info("Successfully logged in!")


@bot.event
async def on_message(message: Message) -> None:
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


async def main():
    await bot.load_extension("cogs.guildsDataUpdate")
    await bot.start(token=config.DISCORD_BOT_TOKEN)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
