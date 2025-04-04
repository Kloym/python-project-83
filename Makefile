install:
	uv sync

dev:
	uv run flask --debug --app page_analyzer:app run

reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

PORT ?= 8000
start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

build:
	./build.sh

render-start:
	gunicorn -w 5 -b 0.0.0.0:10000 page_analyzer:app

lint:
	uv run flake8

