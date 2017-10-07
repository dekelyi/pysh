#!/usr/bin/env python2
import os
import env
from prompt import prompt
from launch import fetch_comm


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
    print prompt(),
    data = raw_input()
    try:
        fetch_comm(data).start()
    except Exception as e:
        print '{0.__class__.__name__}: {0}'.format(e)

init()
while True: main()
