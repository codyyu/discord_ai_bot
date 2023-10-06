from pydantic import BaseModel


class Database(BaseModel):
    user: str
    password: str
    host: str
    port: str
    dbname: str
