ARG BOT_DIR=/bot_runner

FROM python:3.11.5-bullseye
ARG BOT_DIR
RUN mkdir -p ${BOT_DIR}
COPY src/discord_ai_bot ${BOT_DIR}/src/discord_ai_bot
COPY .env poetry.toml pyproject.toml README.md ${BOT_DIR}/
WORKDIR ${BOT_DIR}
RUN python3 -m pip install --upgrade pip
RUN pip install poetry==1.6.1
RUN poetry install --only main
CMD [ "poetry", "run", "python", "src/discord_ai_bot/app.py" ]