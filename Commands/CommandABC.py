from abc import ABCMeta, abstractmethod

class CommandABC:

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        """ Abstract method to run the command """
        return

