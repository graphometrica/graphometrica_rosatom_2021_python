# Python часть решения

## Решение первой задачи

### Вид исходного графа:
![](./data/results/problem_graph.png)

### Общий вид гамильтониана

```
             __           __                _            __
hat{H}  =  A \     (1  -  \     x  )   +  A \     (1  -  \     x  )   +
             /__ i        /__ j  ij         /__ j        /__ i  ij     
                                                                       
                   __              __                                  
                A \               \     x   x         +                
                  /__ u,v notin E /__ j  u,j v,j + 1                   
                                                                       
                   __                __                                
                B \            w    \     x    x                       
                  /__ u,v in E  u,v /__ j  u,j  v, j + 1               

```

`A`, `B` - коэффициенты.

```
B = 1
```

```
A  =  max({w   forall u,v in E})
            u,v                                
```

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
