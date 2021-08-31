import unittest

from matrix_traversal.utils import uri_validator


class MyTestCase(unittest.TestCase):
    def test_valid_uri1(self):
        url = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
        result = uri_validator(url)
        self.assertTrue(result)

    def test_valid_uri2(self):
        url = "http://example.com:80/foo/bar/file.txt"
        result = uri_validator(url)
        self.assertTrue(result)

    def test_random_letters(self):
        url = "asdasvs"
        result = uri_validator(url)
        self.assertFalse(result)

    def test_url_scheme(self):
        url = "/example.com/file.txt"
        result = uri_validator(url)
        self.assertFalse(result)

    def test_url_path(self):
        url = "https://example.com"
        result = uri_validator(url)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
