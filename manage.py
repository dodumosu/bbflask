#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################
#
# management script for barebones flask skeleton
#
################################

import click

from bbflask.factory import create_app
from bbflask.management import commands
from bbflask.management.decorators import pass_config


@click.group()
@pass_config
def cli(config):
    '''Management script for bbflask'''
    if not getattr(config, u'app', None):
        config.app = create_app()

# subcommands
cli.add_command(commands.run)
cli.add_command(commands.shell)


if __name__ == u'__main__':
    cli.main()
