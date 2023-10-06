from datetime import datetime
from typing import Literal

from psycopg2.extensions import connection
from pydantic import BaseModel, Field


class Guilds(BaseModel):
    id: int
    member_count: int
    created_at: datetime
    installed_at: datetime = Field(default=datetime.utcnow())
    status: Literal["Active", "Inactive"]

    def upsert(self, con: connection) -> None:
        query = """
        INSERT INTO guilds(id, member_count, created_at, installed_at, status)
        values (%(id)s, %(member_count)s, %(created_at)s, %(installed_at)s, %(status)s)
        ON CONFLICT (id)
        DO UPDATE
        SET member_count = excluded.member_count,
            created_at = excluded.created_at,
            installed_at = excluded.installed_at,
            status = excluded.status
        """
        with con.cursor() as cur:
            cur.execute(query, self.model_dump())
            con.commit()
