#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'jsonpickle',
    'fastjsonrpc',
    'twisted',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tendril-server-prefab',
    version='0.1.0',
    description="JSON-RPC pre-assembled datasets server using "
                "Twisted for Tendril",
    long_description=readme,
    author="Chintalagiri Shashank",
    author_email='shashank@chintal.in',
    url='https://github.com/chintal/tendril-server-prefab',
    packages=[
        'prefab_server',
    ],
    package_dir={'prefab_server': 'prefab_server'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='tendril-server-prefab',
    classifiers=[
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: MIT License",
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
