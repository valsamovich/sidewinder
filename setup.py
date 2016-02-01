try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Technologies',
    'author': 'Valery Samovich',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/valerysamovich/python-technologies',
    'author_email': 'valerysamovich@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['python-technologies'],
    'scripts': [],
    'name': 'python-technologies'
}

setup(**config)