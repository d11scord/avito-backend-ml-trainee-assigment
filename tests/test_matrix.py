import asyncio
import unittest

from aioresponses import aioresponses

from matrix_traversal.main import get_matrix


class TestGetMatrix(unittest.TestCase):

    def test_get_matrix_base(self):
        source_url = 'https://raw.githubusercontent.com/' \
                     'avito-tech/python-trainee-assignment/main/matrix.txt'
        expected = [
            10, 50, 90, 130,
            140, 150, 160, 120,
            80, 40, 30, 20,
            60, 100, 110, 70,
        ]

        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(get_matrix(source_url))
        self.assertEqual(result, expected)

    def test_1x1_matrix(self):
        matrix_1x1 = "+---+\n" \
                     "| 1 |\n" \
                     "+---+\n"

        expected = [1]

        loop = asyncio.get_event_loop()
        mock_url = "http://test.example.com"
        with aioresponses() as mock:
            mock.get(mock_url, body=matrix_1x1)

            result = loop.run_until_complete(get_matrix(mock_url))
            self.assertEqual(result, expected)

    def test_NxN_matrix(self):
        nxn_matrix = "+-----+-----+-----+-----+\n" \
                     "|  1  |  2  |  3  |  4  |\n" \
                     "+-----+-----+-----+-----+\n" \
                     "|  5  |  6  |  7  |  8  |\n" \
                     "+-----+-----+-----+-----+\n" \
                     "|  9  |  10 |  11 |  12 |\n" \
                     "+-----+-----+-----+-----+\n" \
                     "|  13 |  14 |  15 |  16 |\n" \
                     "+-----+-----+-----+-----+\n"

        expected = [
            1, 5, 9, 13,
            14, 15, 16, 12,
            8, 4, 3, 2,
            6, 10, 11, 7,
        ]

        loop = asyncio.get_event_loop()
        mock_url = "http://test.example.com"
        with aioresponses() as mock:
            mock.get(mock_url, body=nxn_matrix)

            result = loop.run_until_complete(get_matrix(mock_url))
            self.assertEqual(result, expected)

    def test_NxM_matrix(self):
        nxm_matrix = "+-----+-----+-----+-----+\n" \
                     "|  1  |  2  |  3  |  4  |\n" \
                     "+-----+-----+-----+-----+\n" \
                     "|  5  |  6  |  7  |  8  |\n" \
                     "+-----+-----+-----+-----+\n" \
                     "|  9  |  10 |  11 |  12 |\n" \
                     "+-----+-----+-----+-----+\n" \
                     "|  13 |  14 |  15 |  16 |\n" \
                     "+-----+-----+-----+-----+\n" \
                     "|  17 |  18 |  19 |  20 |\n" \
                     "+-----+-----+-----+-----+\n"

        expected = [
            1, 5, 9, 13, 17,
            18, 19, 20, 16, 12,
            8, 4, 3, 2, 6,
            10, 14, 15, 11, 7
        ]

        loop = asyncio.get_event_loop()
        mock_url = "http://test.example.com"
        with aioresponses() as mock:
            mock.get(mock_url, body=nxm_matrix)

            result = loop.run_until_complete(get_matrix(mock_url))
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
