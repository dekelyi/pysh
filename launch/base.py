from abc import ABCMeta, abstractmethod


class Lanchable(object):
    @abstractmethod
    def start(self):
        raise NotImplementedError


class Command(Lanchable):
    def __init__(self, comm, args):
        self.comm = comm
        self.args = args
