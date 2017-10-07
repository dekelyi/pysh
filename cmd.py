#!/usr/bin/env python2
import os
import env
from prompt import prompt
import launch


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
        launch.fetch_comm(data).start()
    except launch._utils.NotSuchCommand as e:
        print 'Not Such Command:', e.args[0]

init()
while True: main()
