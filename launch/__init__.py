from .base import Command as _Command
from .chdir import Chdir as _Chdir


def fetch_comm(commline):
    """
    :type commline: str
    """
    args = commline.split(' ')
    comm = args[0]
    del args[0]

    if comm == 'cd':
        return _Chdir(*args)
    else:
        return _Command(comm, args)