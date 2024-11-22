.PHONY: install-base install-full lint format-code new-app _new-app run migrations migrate migrations-migrate

install-base:
	poetry install --no-dev

install-full:
	poetry install

lint:
	poetry run mypy .

format-code:
	poetry run autoflake . && poetry run isort . && poetry run black .

new-app:
	$(MAKE) _new-app name=$(filter-out $@,$(MAKECMDGOALS))

_new-app:
	cd src && poetry run django-admin startapp $(name)

run:
	cd src && poetry run python manage.py runserver

migrations:
	cd src && poetry run python manage.py makemigrations

migrate:
	cd src && poetry run python manage.py migrate

migrations-migrate:
	make migrations && make migrate

%:
	@: