from abc import ABC, abstractmethod


class Controller(ABC):

    def __init__(self):
        self.kart = None

    def set_kart(self, kart):
        self.kart = kart

    @abstractmethod
    def move(self, string):
        pass
