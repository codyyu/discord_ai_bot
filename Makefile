.PHONY: all, run, format, lint, help

all: help

########################
# Execution
########################
run bot:
	docker-compose -f docker-compose-bot.yml up

run kafka:
	docker-compose -f docker-compose-kafka.yml up

run druid:
	docker-compose -f docker-compose-druid.yml up

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
	@echo 'make format		run code formatter'
	@echo 'make lint		run code linter'
	@echo '============================================='