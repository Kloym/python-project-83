PORT ?= 9000
WORKERS ?= 5
.PHONY: install start-dev start lint build

install:
	uv sync

dev:
	uv run flask --debug --app page_analyzer:app run

reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	uv run flake8

start:
	poetry run flask --app page_analyzer:app --debug run

build:
	./build.sh

render-start:
	poetry run gunicorn --daemon -w $(WORKERS) -b 0.0.0.0:$(PORT) page_analyzer:app

