#!/usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='gevent-websocket2',
      version='1.0',
      py_modules=['geventwebsocket2'],
      install_requires=('gevent-websocket','gevent'),
      url='https://github.com/val-labs/gevent-websocket2.git',
      author='Joel Ward',
      author_email='jmward@gmail.com',
      license='MIT',
      platforms='any',
      )
