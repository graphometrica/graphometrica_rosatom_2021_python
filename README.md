# Python часть решения

## Решение первой задачи

### Вид исходного графа:
![](./data/results/problem_graph.png)

### Общий вид гамильтониана
$$
\hat{H} = A \sum_i (1 - \sum_j x_{ij})^2 + A \sum_j (1 - \sum_i x_{ij})^2 + A \sum_{u,v \notin E} \sum_j x_{u,j}x_{v,j+1} + B \sum_{u,v \in E} w_{u,v} \sum_j x_{u,j} x_{v, j+1}
$$

, где $B = 1$, $A = max({w_{u,v}\text{  }\forall\text{  }u,v \in E})$

- [Конвертер из networkx.Graph в QUBO-матрицу](./solution/converters/tsp2qubo.py)

### Воспроизводимый запуск

- [Установить `poetry`](https://python-poetry.org/docs/#installation)
- Выполнить `make install_dev`
- Выполнить `make run_5_vertices KEY=%API key here%`

### Результаты первой задачи

- [Данные по времени в пути](./data/paths.csv)
- [Матрица смежности графа](./data/results/adjacency.npy)
- [Итоговая QUBO-матрица](./data/results/Q.npy)
- [Найденный путь](./data/results/answer.csv)

### Установка как пакета

- [Установить `poetry`](https://python-poetry.org/docs/#installation)
- Выполнить `make build_and_install_local`

## Python сервис

Более эффективное кодирование через $(N - 1)^2$ спинов: мы считаем, что всегда начинаем из 0-й вершины.

- [Эффективный конвертер из networkx.Graph в QUBO-матрицу](./solution/service/solver/eff_tsp2qubo.py)

Решатель вынесен в отдельную функцию

- [Код решателя](./solution/service/solver/solve.py)

Взаимодействие с `Active MQ` идет с использованием библиотеки `stomp.py`. Валидация данных и сериализация с помощью библиотеки `Pydantic`.

- [Listener](./solution/service/listeners/TSPListener.py)
- [Models](./solution/service/serialization/models.py)
- [Application](./solution/service/app.py)

Входная точка `main.py`. Деплой идете через [Docker](./Dockerfile).
