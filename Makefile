.PHONY: all, bot, kafka, druid, superset, format, lint, setup, help

all: help

########################
# Execution
########################
bot:
	docker compose -f docker-compose-bot.yml up

kafka:
	docker compose -f docker-compose-kafka.yml up

druid:
	docker compose -f docker-compose-druid.yml up

superset:
	docker compose -f superset/docker-compose.yml up

########################
# Linting and Formatting
########################
format:
	poetry run black .
	poetry run isort .

lint:
	poetry run black . --check
	poetry run flake8 .
	poetry run mypy .

#########################
# Set Up
#########################
setup:
	@echo 'Creating .env file'
	touch .env
	@echo "DISCORD_BOT_TOKEN=" >> .env
	@echo "BOT_BACKEND_DATABASE_USERNAME=postgres" >> .env
	@echo "BOT_BACKEND_DATABASE_PASSWORD=postgres" >> .env
	@echo "BOT_BACKEND_DATABASE_HOST=bot_backend_database" >> .env
	@echo "BOT_BACKEND_DATABASE_PORT=5432" >> .env
	@echo "BOT_BACKEND_DATABASE_NAME=discord" >> .env
	@echo 'Please fill in Discord Bot Token manually after setup'
	@echo 'Download HuggingFace Language Model...'
	docker build -t discord/model_init -f ./docker/Dockerfile_model_init ./docker
	docker run -d --rm --name discord-model-init discord/model_init
	docker cp discord-model-init:/build/llm_model ./src/discord_ai_bot/
	docker stop discord-model-init
	docker rmi discord/model_init
	@echo 'Cloning Superset Repo...'
	git clone https://github.com/apache/superset.git



#########################
# Help
#########################
help:
	@echo '============================================='
	@echo 'make bot			instantiate discord bot'
	@echo 'make kafka		instantiate kafka'
	@echo 'make druid		instantiate druid'
	@echo 'make superset	instantiate superset'
	@echo 'make format		run code formatter'
	@echo 'make lint		run code linter'
	@echo 'make setup		set up the environment'
	@echo '============================================='