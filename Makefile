install_dev:
	poetry install
	poetry run pip install --index-url https://repo.qboard.tech/ qboard-client

run_5_vertices:
	poetry run python solve5tsp.py data/results/ $(KEY)

build_and_install_local:
	poetry install --no-dev
	poetry run pip install --index-url https://repo.qboard.tech/ qboard-client
	poetry build
	poetry run pip install .
