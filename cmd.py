#!/usr/bin/env python2
import os
import env
from prompt import prompt


def init():
    # set initial path
    env.Path.set(os.environ['PATH'])

    # set executables extensions
    exts = ['.py']
    if os.name == 'nt':
        exts.extend(['.bat', '.exe'])
    else:
        exts.extend(['.sh', ''])
    env.Executables.set(exts)


def main():
    print prompt(), env.findpath(raw_input())

init()
while True: main()
