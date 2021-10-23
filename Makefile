install_dev:
	poetry install
	poetry run pip install --index-url https://repo.qboard.tech/ qboard-client

run_5_vertices:
	poetry run python solve5tsp.py data/results/ $(KEY)

run_jms:
	poetry run python jmsTest.py
