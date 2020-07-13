from setuptools import setup

setup(
    name='n2w',
    version='0.1.0',
    packages=['n2w'],
    entry_points={
        'console_scripts': [
            'n2w = main:main'
        ]
    })
