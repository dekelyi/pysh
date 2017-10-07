from env import CWD
from .base import Lanchable


class Chdir(Lanchable):
    def __init__(self, path):
        self.path = path

    def start(self):
        CWD.chdir(self.path)
