import asyncio
import unittest

from aiohttp.web_exceptions import HTTPClientError
from aioresponses import aioresponses

from app.matrix import fetch_matrix


class TestResponses(unittest.TestCase):

    def test_500_status(self):
        loop = asyncio.get_event_loop()
        with aioresponses() as mock:
            mock.get('http://example.com', status=500)

            response = loop.run_until_complete(fetch_matrix("http://example.com"))

            self.assertIsNone(response)

    def test_404_status(self):
        loop = asyncio.get_event_loop()
        with aioresponses() as mock:
            mock.get('http://example.com', status=404)

            response = loop.run_until_complete(fetch_matrix("http://example.com"))

            self.assertIsNone(response)

    def test_exception(self):
        loop = asyncio.get_event_loop()
        with aioresponses() as mock:
            mock.get('http://example.com', exception=HTTPClientError())

            response = loop.run_until_complete(fetch_matrix("http://example.com"))

            self.assertIsNone(response)

    # TODO: сделать тест на содержимое файла


if __name__ == '__main__':
    unittest.main()
