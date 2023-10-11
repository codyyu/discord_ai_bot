import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, FilePath
from schema import Database

load_dotenv()


class Config(BaseModel):
    DISCORD_BOT_TOKEN: str = os.environ["DISCORD_BOT_TOKEN"]
    OPENAI_API_KEY: str = os.environ["OPENAI_API_KEY"]
    DATABASE: Database = Database(
        user=os.environ["BOT_BACKEND_DATABASE_USERNAME"],
        password=os.environ["BOT_BACKEND_DATABASE_PASSWORD"],
        host=os.environ["BOT_BACKEND_DATABASE_HOST"],
        port=os.environ["BOT_BACKEND_DATABASE_PORT"],
        dbname=os.environ["BOT_BACKEND_DATABASE_NAME"],
    )
    MODEL_CONFIG_PATH: FilePath = Path(
        os.getcwd(), "src", "discord_ai_bot", "llm_model", "config.json"
    )
    MODEL_PATH: FilePath = Path(
        os.getcwd(), "src", "discord_ai_bot", "llm_model", "pytorch_model.bin"
    )
    TOKENIZER_DIR: FilePath = Path(os.getcwd(), "src", "discord_ai_bot", "llm_model")
