DOCKER_COMPOSE := docker compose
WEB_SERVICE := app

migrations:
	$(DOCKER_COMPOSE) run --rm $(WEB_SERVICE) makemigrations

migrate:
	$(DOCKER_COMPOSE) run --rm -it $(WEB_SERVICE) migrate

checkmigrations:
	$(DOCKER_COMPOSE) run --rm -it $(WEB_SERVICE) migrate --check

run-build:
	$(DOCKER_COMPOSE) up -d --build

run:
	$(DOCKER_COMPOSE) up -d --force-recreate

stop:
	$(DOCKER_COMPOSE) down

createsuperuser:
	$(DOCKER_COMPOSE) run --rm -it $(WEB_SERVICE) createsuperuser

logs:
	$(DOCKER_COMPOSE) logs -f $(WEB_SERVICE)
