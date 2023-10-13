# Discord AI Analytics Bot

## I. Purpose:

To demonstrate the data streaming pipelines by implementing the modern data stack.

## II.  Tech Stack:


- Language: Python 3.9
- Data Source: Discord Bot
- Storage Layer: PostgreSQL
- Streaming Layer: [Apache Kafka](https://kafka.apache.org/)
- Analytics Layer: [Apache Druid](https://druid.apache.org/)
- Visualization Layer: [Apache Superset](https://superset.apache.org/)

## III. Infastructure:
![architecture](./assets/discord_ai_bot_infra.drawio.png)

## IV. Set Up

Due to the scope and purpose of this project, everything will be running in docker containers via simple make commands. Thus, it is essential to have `make`, `docker` and `docker-compose` properly installed. 
#### Pre-requested:
- make
- docker & docker-compose

#### Setup:
- Step 1.\
`make setup`
- Step 2.1.\
Fill in your Discord Bot Token in .env file
- Step 2.2.
    - Find `./superset/docker-compose.yml` file
    - Add `TALISMAN_ENABLED=False` in the `superset` service as an extra environment variable
- Step 3.\
`make kafka`\
Note 1: This step will create a `messages` topic by default\
Note 2: Please make sure all containers are up and running before moving to the next step.
- Step 4.\
`make bot`\
Note 1: This step will instantiate the bot and make the connection to kafka
- Step 5.\
Install the Bot on your Discord Server and type some texts in the Discord channel for testing. Monitoring the Discord Bot log to see if there are any errors.
- Step 7.\
`make druid`
- Step 8. \
`make superset`

## V. Developing Tutorial:
TODO

## VI. Learning Resources:

#### Discord:
- [Doc: discord.py API Documentation](https://discordpy.readthedocs.io/en/stable/)
- [stack overflow: bot cogs usage](https://stackoverflow.com/questions/53528168/how-do-i-use-cogs-with-discord-py)

#### Apache Kafka:
- [Doc: confluent-kafka API Documentation](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html)
- [Youtube: Listener and Advertised Listener Explaination](https://www.youtube.com/watch?v=L--VuzFiYrM&ab_channel=OttoCodes)
- [Github: Confluent Kafka docker-compose Template](https://github.com/confluentinc/cp-all-in-one/tree/7.5.0-post)

#### Apache Druid:

#### Apache Superset: