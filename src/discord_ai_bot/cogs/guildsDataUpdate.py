import logging

from discord import Guild
from discord.ext import commands
from discord.ext.commands import Bot
from psycopg2 import connect
from psycopg2.extensions import connection

from discord_ai_bot.config import Config
from discord_ai_bot.model import Guilds, Members, MembersBatch

logger = logging.getLogger(__name__)
config = Config()


class GuildsDataUpdate(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: Guild) -> None:
        members_list = [
            Members(
                id=member.id,
                guild_id=guild.id,
                name=member.name,
                display_name=member.display_name,
                bot=member.bot,
                status="Active",
                joined_at=member.joined_at,
                created_at=member.created_at,
            )
            for member in guild.members
        ]
        with self.db_connection() as con:
            guilds_data = Guilds(
                id=guild.id,
                member_count=guild.member_count,
                created_at=guild.created_at,
                status="Active",
            )
            members_data = MembersBatch(data=members_list)
            try:
                guilds_data.upsert(con)
                logger.info(f"Successfully update Guild Data for Guild ID: {guild.id}")
                members_data.upsert(con)
                logger.info(
                    f"Successfully update {len(members_list)} Member Data for Guild ID: {guild.id}"
                )
            except Exception as e:
                logger.error(
                    f"Encountering {e} while updating Guilds table and Members table"
                )

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: Guild) -> None:
        with self.db_connection() as con:
            data = Guilds(
                id=guild.id,
                member_count=guild.member_count,
                created_at=guild.created_at,
                status="Deactive",
            )
            try:
                data.deactivate(con)
                logger.info(
                    f"Successfully deactivate Guild Data for Guild ID: {guild.id}"
                )
            except Exception as e:
                logger.error(f"Encountering {e} while deactivating Guild table")

    def db_connection(self) -> connection:
        con = connect(**config.DATABASE.model_dump())
        return con


async def setup(bot: Bot) -> None:
    await bot.add_cog(GuildsDataUpdate(bot))
