import logging

from discord import Message
from discord.ext import commands
from discord.ext.commands import Bot

from discord_ai_bot.config import Config

config = Config()
logger = logging.getLogger(__name__)


class MsgDataUpdate(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:
        pass


async def setup(bot: Bot) -> None:
    await bot.add_cog(MsgDataUpdate(bot))
