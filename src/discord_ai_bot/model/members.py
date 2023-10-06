from datetime import datetime
from typing import Literal

from psycopg2.extensions import connection
from pydantic import BaseModel, Field


class Members(BaseModel):
    id: int
    guild_id: int
    name: str
    display_name: str
    bot: bool
    status: Literal["Active", "Deactive"]
    joined_at: datetime
    created_at: datetime
    updated_at: datetime = Field(default=datetime.utcnow())

    def upsert(self, con: connection) -> None:
        query = """
        INSERT INTO members(id, guild_id, name, display_name, bot, status, joined_at, created_at, updated_at)
        VALUES (%(id)s, %(guild_id)s, %(name)s, %(display_name)s, %(bot)s, %(status)s, %(joined_at)s, %(created_at)s, %(updated_at)s)
        ON CONFLICT (id, guild_id)
        SET name = excluded.name
            display_name = excluded.display_name,
            bot = excluded.bot,
            status = excluded.status,
            joined_at = excluded.joined_at,
            created_at = excluded.created_at,
            updated_at = excluded.updated_at
        """
        with con.cursor() as cur:
            cur.execute(query, self.model_dump())
            con.commit()

    def deativate(self, con: connection) -> None:
        pass

    def delete(self, con: connection) -> None:
        pass


class MembersBatch(BaseModel):
    data: list[Members]

    def upsert(self, con: connection) -> None:
        with con.cursor() as cur:
            args = ",".join(
                cur.mogrify(
                    "(%(id)s, %(guild_id)s, %(name)s, %(display_name)s, %(bot)s, %(status)s, %(joined_at)s, %(created_at)s, %(updated_at)s)",
                    i.model_dump(),
                ).decode("utf-8")
                for i in self.data
            )
            query = f"""
            INSERT INTO members(id, guild_id, name, display_name, bot, status, joined_at, created_at, updated_at)
            VALUES {args}
            """
            cur.execute(query)
            con.commit()
