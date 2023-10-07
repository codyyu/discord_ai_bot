import json
import logging
from typing import Union

from confluent_kafka import KafkaError
from confluent_kafka import Message as KF_Message
from confluent_kafka import Producer
from discord import Message
from discord.ext import commands
from discord.ext.commands import Bot

from discord_ai_bot.config import Config

config = Config()
logger = logging.getLogger(__name__)

# instantiate kafka producer
producer = Producer(
    {"bootstrap.servers": "broker:29092", "client.id": "Discord-Message"}
)


def msg_callback(err: Union[KafkaError, None], msg: KF_Message) -> None:
    if err:
        logger.error(f"Failed to deliver msg via kafka: {err}")
    else:
        logger.info(f"Produced event to topic: {msg.topic()}")


class MsgDataUpdate(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:
        topic = "messages"
        msg = {
            "message_id": message.id,
            "message_content": message.content,
            "member_id": message.author.id,
        }
        producer.produce(
            topic=topic, key="message", value=json.dumps(msg), callback=msg_callback
        )
        producer.poll(1)
        producer.flush()


async def setup(bot: Bot) -> None:
    await bot.add_cog(MsgDataUpdate(bot))
