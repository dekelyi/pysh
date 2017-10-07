import os

from .envitem import ListEnv
from .cwd import WorkingDirectory


ENV_PATH = 'PYSH_PATH'
ENV_EXE = 'PYSH_EXES'
ENV_CWD = 'CD' if os.name == 'nt' else 'PWD'

Path = ListEnv(ENV_PATH)
Executables = ListEnv(ENV_EXE)
CWD = WorkingDirectory(ENV_CWD)


def findpath(prog):
    """
    Find the full path of a script
    :param str prog: Program name to find
    :rtype: str
    """
    for path in Path.getlist():
        for exe in Executables.getlist():
            full = os.path.join(path, prog + exe)
            if os.path.isfile(full):
                return full
