import asyncio
from argparse import ArgumentParser
from typing import List, Optional

from app.matrix import fetch_matrix, snail, clean_matrix


async def get_matrix(url: str) -> Optional[List[int]]:
    """
    :param url: URL для загрузки матрицы с сервера
    :return: Список, содержащий результат обхода полученной матрицы по спирали
    """

    # Сходить по ссылке.
    # Распарсить числа из символов.
    matrix = await fetch_matrix(url)
    if matrix:
        matrix = clean_matrix(matrix)
        matrix = snail(matrix)

        print("Here is your beautiful snailed matrix:")
        print(matrix)

        return matrix


if __name__ == '__main__':
    arg_parser = ArgumentParser(
        description="Traverse the matrix in a counterclockwise spiral pattern.")
    arg_parser.add_argument(
        "url", help="source URL for matrix", type=str,
    )
    args = arg_parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_matrix(args.url))
