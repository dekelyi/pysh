from abc import ABCMeta, abstractmethod

from env import CWD


class Lanchable(object):
    @abstractmethod
    def start(self):
        pass


class Command(Lanchable):
    def __init__(self, comm, args):
        self.comm = comm
        self.args = args


class Chdir(Lanchable):
    def __init__(self, path):
        self.path = path
    
    def start(self):
        CWD.chdir(self.path)
