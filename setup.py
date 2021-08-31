# https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14

from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="matrix-traversal",
    version="0.1.0",
    description="Library for counterclockwise traversal of a matrix.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="127.0.0.1",
    author="Julia Kuzkina",
    author_email="juliakuzkina1@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["matrix_traversal"],
    include_package_data=True,
    install_requires=["aiohttp"],
    tests_require=["aioresponses==0.7.2"],
    test_suite="tests",
)
