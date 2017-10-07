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
    print env.findpath(data)
    print fetch_comm(data)
    fetch_comm(data).start()

init()
while True: main()
