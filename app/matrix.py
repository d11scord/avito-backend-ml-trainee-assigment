import aiohttp
from typing import List


async def fetch_matrix(url: str):
    """
    Функция для похода на сервер

    :param url: Ссылка для загрузки матрицы
    :return: Матрица без форматирования
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            print("Response status:", response.status)
            raw_matrix = await response.text()
            print(raw_matrix)
            print(clean_matrix(raw_matrix))

    # TODO: добавить обработчик ошибок


def clean_matrix(raw_matrix: str):
    """
    Функция для удаления форматирования

    :param raw_matrix: Матрица с форматированием.
    :return: Список строк матрицы
    """
    raw_matrix = raw_matrix.split("\n")
    raw_matrix = [
        row.replace("+", "").replace("-", "").replace("|", "").split()
        for row in raw_matrix[1::2]  # Скипаем +---+---+---+---+
    ]
    matrix = list()

    for row in raw_matrix:
        # TODO: откуда-то берётся пустой массив
        if not row:
            continue
        matrix.append(list(map(int, row)))

    return matrix


def snail(matrix: List[List[int]]) -> List[int]:
    """
    Функция для обхода матрицы по спирали

    :param matrix: Список строк матрицы
    :return: Список после обхода матрицы
    """

    result = list()

    matrix = list(zip(*matrix))
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]

    return result
