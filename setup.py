# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='tc_librato',
    version="0.0.1",
    description='Thumbor Librato extensions',
    author='Peter Schröder, Sebastian Eichner',
    author_email='peter.schroeder@jimdo.com, sebastian.eichner@jimdo.com',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'thumbor-latest',
        'librato-metrics',
    ]
)
