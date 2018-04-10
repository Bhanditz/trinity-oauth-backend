#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0111,W6005,W6100

import os
import re

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('trinity_oauth_backend', '__init__.py')

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='trinity-oauth-backend',
    version=VERSION,
    description='An OAuth backend for Texas Gateway (Trinity), mostly used for Open edX but can be used elsewhere.',
    long_description=README,
    author='Omar Al-Ithawi',
    author_email='omar@appsembler.com',
    url='https://github.com/appsembler/trinity-oauth-backend',
    packages=[
        'trinity_oauth_backend',
    ],
    include_package_data=True,
    zip_safe=False,
    keywords='Appsembler OAuth Trinity Texas-Gateway',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)
