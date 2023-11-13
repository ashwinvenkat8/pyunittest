from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, '.version'), encoding='utf-8') as f:
    version = f.read()

with open(path.join(here, '.env'), encoding='utf-8') as f:
    author_info = f.readlines()
    author = author_info[0].strip()
    author_email = author_info[1].strip()
    author_gh = author_info[2].strip()

setup(
    name = 'pyunittest',
    version = version,
    description = 'A lightweight, Python unit testing module for small-scale scripts.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    keywords = 'python unit testing, lightweight unit testing',
    author = author,
    author_email = author_email,
    url = f'https://github.com/{author_gh}/pyunittest',
    packages = find_packages(),
    package_dir = {
        'pyunittest': 'pyunittest'
    },
    package_data = {
        'pyunittest': [
            'bin/*',
            '../.version'
        ]
    }
)
