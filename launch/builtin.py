import os
from pkgutil import iter_modules
from .base import Lanchable
from . import _builtins


BUILTINS = os.path.split(_builtins.__file__)[0]


def has(name):
    for _, module, _ in iter_modules([BUILTINS]):
        if name == module:
            return True
    return False


def _get(name):
    return getattr(_builtins, name)


def get(comm, *args, **kwargs):
    return Builtin(comm, *args, **kwargs)


class Builtin(Lanchable):
    def run(self):
        _get(self._comm).main(*self._args, **self._kwargs)
