from abc import ABCMeta, abstractmethod


class Lanchable(object):
    def __init__(self, comm, *args, **kwargs):
        self._comm = comm
        self._args = args
        self._kwargs = kwargs

    def _start(self):
        try:
            self.run()
        except Exception as e:
            print '{0.__class__.__name__}: {0}'.format(e)
        except (SystemExit, KeyboardInterrupt):
            pass

    start = _start

    @abstractmethod
    def run(self):
        raise NotImplementedError
