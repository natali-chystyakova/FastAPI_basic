.PHONY: d-project-i-run
# Make all actions needed for run homework from zero.
d-project-i-run:
	make d-run

.PHONY: d-project-i-purge
# Make all actions needed for purge homework related data.
d-project-i-purge:
	@make d-purge


.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose up --build

.PHONY: d-stop
# Stop services
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down

.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

# .PHONY: homework-i-run
# # Run homework.
# homework-i-run:
# 	@python main.py
#
# .PHONY: homework-i-purge
# homework-i-purge:
# 	@echo Goodbye


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files