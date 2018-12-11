from abc import *


class WeichenControlInterface(ABC):

    @abstractmethod
    def initialisation(self):
        pass

    @abstractmethod
    def de_initialisation(self):
        pass

    @abstractmethod
    def turnout_set_for_route(self, str_addr_low, str_addr_high, bol_color):
        pass

    @abstractmethod
    def turnout_free(self, str_addr_low, str_addr_high):
        pass