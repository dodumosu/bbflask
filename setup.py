# -*- coding: utf-8 -*-
from setuptools import setup

setup(
        name=u'bbflask',
        version=u'0.1',
        py_modules=[u'manage'],
        install_requires=[
            u'Click',
        ],
        entry_points=u'''
        [console_scripts]
        bbflask-cli=manage:cli
        ''',
)
