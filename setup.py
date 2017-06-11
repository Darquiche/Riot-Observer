# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

from riot_observer import *

setup(
    name='riot_observer',
    version=observer.__version__,
    packages=find_packages(),
    author="Darqi",
    description="Python light wrapper for the Riot Games API for League of Legends",
    long_description=open('README.md').read(),
    include_package_data=True,
    url='https://github.com/Darquiche/Riot-Observer',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'Topic :: Games/Entertainment :: Role-Playing'
    ],
    license='MIT',
    keywords='league of legends riot games api wrapper development python',
    install_requires=[
        'requests'
    ]
)
