.PHONY: all, format, lint

all: help

########################
# Execution
########################

run:
	docker-compose up

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