#!/usr/bin/env python3

from distutils.core import setup
import os

setup(  name='Paul',
        version='1.0.0',
        url='https://github.com/methanol/paul',
        description='Paul is a commandline tool to send push notifications via prowl to your smartphone',
        long_description=open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r').read(),
        author='Timo Schrappe',
        author_email='schrappe.t@thirdman.de',
        py_modules=['paul'],
        scripts=['bin/paul'],
        license='MIT'
)
