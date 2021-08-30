import asyncio
from typing import List, Optional

import aiohttp
from aiohttp import ClientConnectorError, ServerConnectionError, ServerTimeoutError
from aiohttp.web_exceptions import HTTPClientError, HTTPServerError


async def fetch_matrix(url: str) -> Optional[str]:
    """
    Функция для похода на сервер

    :param url: Ссылка для загрузки матрицы
    :return: Матрица без форматирования
    """

    # TODO: сделать покрасивее
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.get(url=url)
            raw_matrix = await response.text()  # TODO: а вдруг большой файл?
    except (asyncio.TimeoutError, ServerTimeoutError):
        print("ERROR: Timeout")
    except HTTPClientError:  # 4xx
        print("ERROR: Проверьте введённый URL")
    except (HTTPServerError, ServerConnectionError):  # 5xx
        print("ERROR: Сервер недоступен. Попробуйте позже")
    except ClientConnectorError:
        print("ERROR: Проверьте соединение")
    except Exception as e:
        print("ERROR: Произошло что-то непонятное... Попробуйте ещё раз", str(e))
    else:
        if response.status >= 500:
            print("ERROR [Response status {}]: Сервер недоступен. "
                  "Попробуйте подключиться позже".format(response.status))
        elif 400 <= response.status < 500:
            print("ERROR [Response status {}]: "
                  "Проверьте введённый URL".format(response.status))
        elif response.status == 200:
            return raw_matrix
        return None


def clean_matrix(raw_matrix: str) -> List[List[int]]:
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
