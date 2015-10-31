# -*- coding: utf-8 -*-
import click


class CommandConfig(object):
    '''A click utility class for passing around command data.'''
    def __init__(self):
        self.app = None

pass_config = click.make_pass_decorator(CommandConfig, ensure=True)
