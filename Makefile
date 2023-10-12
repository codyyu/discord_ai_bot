.PHONY: all, bot, kafka, druid, format, lint, help

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
# Help
#########################
help:
	@echo '============================================='
	@echo 'make bot			instantiate discord bot'
	@echo 'make kafka		instantiate kafka'
	@echo 'make druid		instantiate druid'
	@echo 'make format		run code formatter'
	@echo 'make lint		run code linter'
	@echo '============================================='