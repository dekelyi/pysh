import os
import collections

ENV_SEP = ';' if os.name == 'nt' else ':'


class EnvItem(object):
    """
    An Environemnt Item
    """

    def __init__(self, name):
        """
        :type name: str
        """
        self.name = name

    def get(self):
        """
        :rtype: str
        """
        return os.environ[self.name]

    def set(self, val):
        """
        :param str val: value
        """
        os.environ[self.name] = val


class ListEnv(EnvItem):
    """
    An environment item that is represent by a list
    """
    def __init__(self, name, sep=ENV_SEP):
        """
        :type name: str
        :type sep: str
        """
        super(ListEnv, self).__init__(name=name)
        self.sep = sep

    def getlist(self):
        """
        :rtype: list[str]
        """
        return self.get().split(self.sep)

    def set(self, val):
        """
        :param str | collections.Sequence val: value of path
        :raise TypeError: unknown type of value
        """
        if isinstance(val, str):
            super(ListEnv, self).set(val)
        elif isinstance(val, collections.Sequence):
            os.environ[self.name] = self.sep.join(val)
        else:
            raise TypeError

    def add(self, val):
        """
        :param str val: value to add
        """
        lst = self.getlist()
        lst.append(val)
        self.set(val)
