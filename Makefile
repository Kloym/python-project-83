install:
	uv sync

dev:
	uv run flask --debug --app page_analyzer:app run

reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	uv run flake8

start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

build:
	./build.sh

render-start:
	source .venv/bin/activate && /opt/render/project/src/.venv/bin/gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

