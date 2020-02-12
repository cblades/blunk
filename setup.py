# -*- coding: utf-8 -*-
"""Setup for blunk."""
from setuptools import setup, find_packages

version = '1.0.0'

install_requires = []


setup(
    author='Chris Blades',
    description='Simple signaling for python.  Like blinker but stupider.',
    download_url='https://github.com/cblades/blunk/tarball/{}'.format(version),
    include_package_data=True,
    install_requires=install_requires,
    license='GNU GENERAL PUBLIC LICENSE, Version 3',
    name='blunk',
    packages=find_packages(),
    url='https://github.com/cblades/blunk',
    version=version,
    zip_safe=True,
)