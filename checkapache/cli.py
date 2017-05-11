# -*- coding: utf-8 -*-

import click
import argparse


def _display_menu():
    print 'TBC'


def _run_update():
    return ('TBC')
    # Backup the file
    # Do the replacements
    # Inform user of backup + new file name


@click.command()
@click.option('--file', help='Full path to an Apache httpd.conf file.')
@click.option('--update', is_flag=True, help='Generate a new config file?')
def main(file, update):
    """Console script for checkapache"""
    _display_menu()
    # click.echo("Put code into checkapache.cli.main")
    # click.echo("See click documentation at http://click.pocoo.org/")
    if update:
        _run_update()


if __name__ == "__main__":
    main()
