try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup

config = [
    'description' : 'A simple program that returns the text of a page from wikipedia given its title',
    'author': 'Lance Lansing',
    'author_email': 'colelansing@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['wiki_reader'],
    'scripts': [],
    'name': 'wiki_reader'
]

setup(**config)