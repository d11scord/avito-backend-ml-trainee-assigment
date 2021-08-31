# https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not/38020041#38020041

from urllib.parse import urlparse, ParseResult


a = "https://file.txt"


def uri_validator(uri: str):
    result: ParseResult = urlparse(uri)
    return result.scheme in ["http", "https"] and all([result.netloc, result.path])


print(uri_validator(a))
