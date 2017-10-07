import os
from pkgutil import iter_modules
from importlib import import_module

from . import _utils


def fetch_comm(commline):
    """
    :type commline: str
    """
    args = commline.split(' ')
    comm = args[0]
    del args[0]

    for _, module, _ in iter_modules([os.path.dirname(__file__)]):
        mod = import_module('{}.{}'.format(__name__, module))
        if not hasattr(mod, 'has'):
            continue
        if mod.has(comm):
            return mod.get(comm, *args)
    
    raise _utils.NotSuchCommand(comm)
