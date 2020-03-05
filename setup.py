"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'readME.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'git_tag.txt'), encoding='utf-8') as f:
    version = f.readline().strip('\n')

setup(
    name='common-utilities',

    version=version,

    description='Shared set of utitlity classes',
    long_description=long_description,

    url='https://github.com/LandRegistry',

    author='HM Land Registry',
    author_email='test@landregistry.gov.uk',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],

    keywords='development',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['flask']
)
