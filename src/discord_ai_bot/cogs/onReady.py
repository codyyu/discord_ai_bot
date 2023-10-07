import logging

from discord.ext import commands
from discord.ext.commands import Bot

from discord_ai_bot.config import Config

config = Config()


logger = logging.getLogger(__name__)


class OnReady(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        logger.info("Successfully logged in!")


async def setup(bot: Bot) -> None:
    await bot.add_cog(OnReady(bot))
