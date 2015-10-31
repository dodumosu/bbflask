# -*- coding: utf-8 -*-
import code

import click

from bbflask.management.decorators import pass_config


@click.command()
@pass_config
def shell(config):
    '''Starts up an interactive shell.'''
    context = {u'app': config.app}

    # attempt to use IPthon if it's installed
    try:
        try:
            # IPython 0.10.x
            from IPython.Shell import IPShellEmbed
            ipshell = IPShellEmbed()
            ipshell(global_ns={}, local_ns={})
        except ImportError:
            # IPython 0.12+
            from IPython import embed
            embed(user_ns=context)
        return
    except ImportError:
        pass

    code.interact(None, local=context)


@click.command()
@click.option('--host', default=None, help='Host to run on')
@click.option('--port', default=None, help='Port to run on', type=int)
@pass_config
def run(config, host, port):
    '''Start up the development server.'''
    config.app.run(host=host, port=port)

