import json
import logging
from typing import Union

from confluent_kafka import KafkaError
from confluent_kafka import Message as KF_Message
from confluent_kafka import Producer
from discord import Message
from discord.ext import commands
from discord.ext.commands import Bot
from transformers import (
    AutoConfig,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    pipeline,
)

from discord_ai_bot.config import Config

config = Config()
logger = logging.getLogger(__name__)

# instantiate kafka producer
producer = Producer(
    {"bootstrap.servers": "broker:29092", "client.id": "Discord-Message"}
)

# instantiate HuggingFace Pipeline
model_config = AutoConfig.from_pretrained(config.MODEL_CONFIG_PATH)
model = AutoModelForSequenceClassification.from_pretrained(
    config.MODEL_PATH, config=model_config
)
tokenizer = AutoTokenizer.from_pretrained(config.TOKENIZER_DIR)
pipe = pipeline(
    model="cardiffnlp/twitter-roberta-base-hate-latest",
    tokenizer=tokenizer,
    task="text-classification",
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
        # identify message hateful score
        result = pipe(message.content)[0]
        is_hate = True if result["label"] == "HATE" else False
        score = round(result["score"] * 100, 2)

        topic = "messages"
        msg = {
            "message_id": message.id,
            "message_content": message.content,
            "member_id": message.author.id,
            "is_bot": message.author.bot,
            "is_hate": is_hate,
            "is_hate_score": score,
            "guild_id": message.guild.id,
            "channel_id": message.channel.id,
            "sent_at": message.created_at,
        }
        producer.produce(
            topic=topic, value=json.dumps(msg, default=str), callback=msg_callback
        )
        producer.poll(1)
        producer.flush()


async def setup(bot: Bot) -> None:
    await bot.add_cog(MsgDataUpdate(bot))
