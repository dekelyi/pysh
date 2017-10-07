import argparse
from env import CWD


def adopt():
    """
    :rtpye: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(prog='cd', description='Chane working directory')
    parser.add_argument('path', metavar='PATH', default='~')
    return parser


def main(*args):
    arguments = adopt().parse_args(args)
    CWD.chdir(arguments.path)
