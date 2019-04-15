from setuptools import setup

requires = [
    'bcrypt',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_tm',
    'psycopg2',
    'sqlalchemy',
    'waitress',
    'zope.sqlalchemy',
]

setup(
    name='login',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = login:main'
        ],
        'console_scripts': [
            'initialize_db = login.initialize_db:main'
        ],
    },

)