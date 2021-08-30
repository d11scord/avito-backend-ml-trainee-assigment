import asyncio
import os
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

    if not url:
        return print("ERROR: Необходимо указать ссылку на матрицу")

    # TODO: сделать покрасивее
    try:
        async with aiohttp.ClientSession() as session:

            response = await session.get(url=url)
            if response.status >= 500:
                print("ERROR [Response status {}]: Сервер недоступен. "
                      "Попробуйте подключиться позже".format(response.status))
            elif 400 <= response.status < 500:
                print("ERROR [Response status {}]: "
                      "Проверьте введённый URL".format(response.status))
            else:
                # Пишем в файл, потому что вдруг матрица очень большая.
                raw_matrix_filename = "raw_matrix.txt"
                chunk_size = 1024
                with open(raw_matrix_filename, 'wb') as fd:
                    while True:
                        chunk = await response.content.read(chunk_size)
                        if not chunk:
                            break
                        fd.write(chunk)
                return raw_matrix_filename

    except (asyncio.TimeoutError, ServerTimeoutError):
        print("ERROR: Timeout")
    except HTTPClientError:  # 4xx
        print("ERROR: Проверьте введённый URL и соединение с сетью")
    except (HTTPServerError, ServerConnectionError):  # 5xx
        print("ERROR: Сервер недоступен. Попробуйте позже")
    except ClientConnectorError:
        print("ERROR: Проверьте соединение")
    except Exception:
        print("ERROR: Произошло что-то непонятное... Попробуйте ещё раз")


def clean_matrix(raw_matrix_path: str) -> List[List[int]]:
    """
    Функция для удаления форматирования

    :param raw_matrix_path: Файл, содержащий матрицу с форматированием
    :return: Список строк матрицы без форматирования
    """

    with open(raw_matrix_path) as file:
        raw_matrix = file.readlines()

    raw_matrix = [
        row.replace("+", "").replace("-", "").replace("|", "").split()
        for row in raw_matrix[1::2]  # Скипаем форматирование
    ]
    matrix = list()

    # Не держим в памяти две матрицы.
    # Одна постепенно переходит в другую.
    while raw_matrix:
        row = raw_matrix.pop(0)
        matrix.append(list(map(int, row)))

    if os.path.exists(raw_matrix_path):
        os.remove(raw_matrix_path)

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
