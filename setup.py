#!/usr/bin/env python3

# Copyright (C) 2018 KANO Computing <dev@kano.me>
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2


from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='fsdiff',
    version='0.4.3',
    description='Byte to byte comparison of local disk images or filesystems',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='KANO Computing',
    author_email='dev@kano.me',
    url='https://github.com/KanoComputing/fsdiff',
    python_requires='>=3.0',
    packages=['fsdiff'],
    scripts=['bin/fsdiff'],
    install_requires=[
        "colorama"
    ],
    platforms='POSIX',
    license='GNU GPL v2'
)
