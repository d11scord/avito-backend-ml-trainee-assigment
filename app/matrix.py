from typing import List

import aiohttp


async def fetch_matrix(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            print("Response status:", response.status)
            raw_matrix = await response.text()
            print(raw_matrix)
