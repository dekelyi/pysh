import os

from .envitem import EnvItem


class WorkingDirectory(EnvItem):
    def chdir(self, path):
        """
        Change dirctory

        :param str path: relative path
        """
        path = os.path.expanduser(path)
        if os.name != 'nt' and path.startswith('/'):
            pass
        elif os.path.splitdrive(path)[0]:
            pass
        else:
            path = os.path.join(self.get(), path)
        path = os.path.abspath(path)
        os.chdir(path)
        self.set(path)
