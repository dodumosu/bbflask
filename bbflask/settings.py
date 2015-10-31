# -*- coding: utf-8 -*-
from prettyconf import config
from unipath import Path

PROJECT_NAME = u'BBFlask'
PROJECT_ROOT = Path().parent

config.starting_path = PROJECT_ROOT.parent.absolute()

DEBUG = config(u'DEBUG', default=True, cast=config.boolean)
