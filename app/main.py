from typing import List

from app.matrix import fetch_matrix, snail, clean_matrix


async def get_matrix(url: str) -> List[int]:
    """
    :param url: URL для загрузки матрицы с сервера
    :return: Список, содержащий результат обхода полученной матрицы по спирали
    """

    # Сходить по ссылке.
    # Распарсить числа из символов.

    matrix = await fetch_matrix(url)
    matrix = clean_matrix(matrix)
    matrix = snail(matrix)

    print("Here is your beautiful snailed matrix:")
    print(matrix)

    return matrix

    # Не забыть про обработку ошибок.
