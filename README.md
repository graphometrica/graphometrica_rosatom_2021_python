# Python часть решения

# Ключевые части

- [Данные по времени в пути](./data/paths.csv)
- [Матрица смежности графа](./data/results/initial_adj.csv)
- [Конвертер из networkx.Graph в QUBO-матрицу](./solution/converters/tsp2qubo.py)
- [Итоговая QUBO-матрица](./data/results/QUBO.csv)
- [Найденный путь](./data/results/graph_path.csv)

# Воспроизводимый запуск

- [Установить `poetry`](https://python-poetry.org/docs/#installation)
- Выполнить `make install_dev`
- Выполнить `make run_5_vertices`
