from datetime import datetime
from typing import Literal

from psycopg2.extensions import connection
from pydantic import BaseModel, Field


class Guilds(BaseModel):
    id: int
    member_count: int
    created_at: datetime
    installed_at: datetime = Field(default=datetime.utcnow())
    status: Literal["Active", "Deactive"]
    updated_at: datetime = Field(default=datetime.utcnow())

    def upsert(self, con: connection) -> None:
        query = """
        INSERT INTO guilds(id, member_count, created_at, installed_at, status, updated_at)
        values (%(id)s, %(member_count)s, %(created_at)s, %(installed_at)s, %(status)s, %(updated_at)s)
        ON CONFLICT (id)
        DO UPDATE
        SET member_count = excluded.member_count,
            created_at = excluded.created_at,
            installed_at = excluded.installed_at,
            status = excluded.status,
            updated_at = excluded.updated_at
        """
        with con.cursor() as cur:
            cur.execute(query, self.model_dump())
            con.commit()

    def deactivate(self, con: connection) -> None:
        query = f"""
        UPDATE guilds
        SET status = '{self.status}',
            updated_at = '{self.updated_at}'
        WHERE id = '{self.id}'
        """
        with con.cursor() as cur:
            cur.execute(query)
            con.commit()

    def delete(self, con: connection) -> None:
        query = f"""
        DELETE FROM guilds
        WHERE id = '{self.id}'
        """
        with con.cursor() as cur:
            cur.execute(query)
            con.commit()
