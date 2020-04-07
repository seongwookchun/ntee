# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='test_package',
    version='0.0.1',
    author='csw',
    author_email='chun3842@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tntee=tntee.tcli:tcli'
        ]
    }
)
