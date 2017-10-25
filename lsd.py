#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import argparse

FILENAME = "./.lsd.yaml"


def parse():
    """help
    -l look
    -c add comment, added time
    -f filename
    -i interpreter mode
    -h show this message
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help='look at lsa.yaml in a pretty way', default=True, action='store_false', dest='is_print')
    parser.add_argument('-c', help='add a comment', type=str, dest='comment')
    parser.add_argument('-f', help='select a filename or directory name', type=str, dest='filename')
    parser.add_argument('-i', help='start interpriter mode', default=False, dest='is_interprit', action='store_true')
    args = parser.parse_args()
    return args


def interprint():
    """
    selectable mode.
    printする？(y/n)
    add commentする？(y/n)
        select file or directory:
        add comment:
    """
    pass


def pretty_print():
    """
    load YAML, and then print it
    """
    pass


def add_comment():
    """
    load YAML, and add some info, save it and overwrite to YAML
    """
    pass


def check_exist():
    """
    .lsd.yamlが存在するかを確認する
    """
    return True


def first_commit():
    """
    touch .lsd.yaml
    """
    pass


def add_error():
    """
    error構文をprint
    """
    pass


def lsd():
    args = parse()

    if args.is_interprit:
        interprit()

    else:
        if args.is_print:
            pretty_print()

        if args.comment and args.filename:
            add_comment()
        elif not args.comment and not args.filename:
            pass
        else:
            add_error()


if __name__ == '__main__':
    lsd()
