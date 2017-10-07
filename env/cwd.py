import os

from .envitem import EnvItem


class WorkingDirectory(EnvItem):
    def chdir(self, path):
        """
        Change dirctory

        :param str path: relative path
        """
        if os.name != 'nt' and path.startswith('/'):
            pass
        elif os.path.splitdrive(path)[0]:
            pass
        else:
            path = os.path.join(self.get(), path)
        self.set(os.path.abspath(path))
