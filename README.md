# Python Backend ML Assigment

## Запуск проекта

На `Python 3.8` и выше без установки проекта как библиотеки:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python -m matrix_traversal [URL]
```

Установка в качестве библиотеки:

```
pip install .

python matrix_traversal [URL]
```

С помощью `Docker`:

```
docker build -t matrix_traversal .

docker run --rm matrix_traversal [URL]
```

## Пример работы

```python
import asyncio
from matrix_traversal import get_matrix

url = "https://raw.githubusercontent.com/" \
      "avito-tech/python-trainee-assignment/main/matrix.txt"

loop = asyncio.get_event_loop()
matrix = loop.run_until_complete(get_matrix(url))

print(matrix)
# [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
```

## Тестирование

```
python -m unittest -v
```
