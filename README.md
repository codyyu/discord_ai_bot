# Discord AI Analytics Bot

## I. Purpose:

To demonstrate the data streaming pipelines by implementing the modern data stack.

## II.  Tech Stack:


- Language: Python 3.11
- Data Source: Discord Bot
- Storage Layer: PostgreSQL
- Streaming Layer: [Apache Kafka](https://kafka.apache.org/)
- Analytics Layer: [Apache Druid](https://druid.apache.org/)
- Visualization Layer: [Apache Superset](https://superset.apache.org/)

## III. Infastructure:
TODO

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
`make kafka`
- Step 4.\
`make druid`
- Step 5.\
`make superset`
- Step 6. \
`make bot`
- Step 7.\
Install the Bot on your Discord Server

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