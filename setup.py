# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='imdbProject',
    version='0.1.0',
    description='Python ETL Project w/ RESTful API',
    long_description=readme,
    author='Michael McArthur',
    author_email='michael.mcarthur94@hotmail.co.uk',
    url='https://github.com/michaelmaca/imdbProject',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

