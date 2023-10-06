import logging

from discord import Guild
from discord.ext import commands
from discord.ext.commands import Bot
from psycopg2 import connect
from psycopg2.extensions import connection

from discord_ai_bot.config import Config
from discord_ai_bot.model import Guilds

config = Config()
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)
handler.setLevel(logging.INFO)


class GuildsDataUpdate(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: Guild) -> None:
        with self.db_connection() as con:
            data = Guilds(
                id=guild.id,
                member_count=guild.member_count,
                created_at=guild.created_at,
                status="Active",
            )
            try:
                data.upsert(con)
                logger.info(f"Successfully update Guild Data for Guild ID: {guild.id}")
            except Exception as e:
                logger.error(f"Encountering {e} while updating Guild table")

    def db_connection(self) -> connection:
        con = connect(**config.DATABASE.model_dump())
        return con


async def setup(bot):
    await bot.add_cog(GuildsDataUpdate(bot))
