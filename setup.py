# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
from setuptools import setup, find_packages


if __name__ == '__main__':
    print('Sopel does not correctly load modules installed with setup.py '
          'directly. Please use "pip install .", or add {}/sopel_modules to '
          'core.extra in your config.'.format(
              os.path.dirname(os.path.abspath(__file__))),
          file=sys.stderr)

script_dir = os.path.dirname(os.path.realpath(__file__))

with open('{}/README.md'.format(script_dir)) as readme_file:
    readme = readme_file.read()

with open('{}/NEWS'.format(script_dir)) as history_file:
    history = history_file.read()

with open('{}/requirements.txt'.format(script_dir)) as requirements_file:
    requirements = [req for req in requirements_file.readlines()]

setup(
    name='sopel_modules.trakt',
    version='0.1.0',
    description='A sopel plugin that returns the user\'s last play on trakt',
    long_description=readme + '\n\n' + history,
    author='Shane Donohoe',
    author_email='shane@donohoe.cc',
    url='https://github.com/shanedabes/sopel-trakt',
    packages=find_packages('.'),
    namespace_packages=['sopel_modules'],
    include_package_data=True,
    install_requires=requirements,
    #  tests_require=dev_requirements,
    test_suite='tests',
    license='Eiffel Forum License, version 2',
)
