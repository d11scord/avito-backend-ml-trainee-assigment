from typing import List

import aiohttp


async def fetch_matrix(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            print("Response status:", response.status)
            raw_matrix = await response.text()
            print(raw_matrix)
            print(clean_matrix(raw_matrix))


def clean_matrix(raw_matrix: str):
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
