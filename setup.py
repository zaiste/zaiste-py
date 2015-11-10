from distutils.core import setup

setup(
    name = 'zaiste',
    version = '0.1.0',
    description = 'A Python package example',
    author = 'Zaiste',
    author_email = 'oh@zaiste.net',
    url = 'https://github.com/zaiste/zaiste-py', 
    py_modules=['zaiste'],
    install_requires=[
      # list of this package dependencies
    ],
    entry_points='''
        [console_scripts]
        zaiste=zaiste:cli
    ''',
)