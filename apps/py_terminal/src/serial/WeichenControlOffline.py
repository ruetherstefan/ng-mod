from src.serial.WeichenControlInterface import *


class WeichenControlOffline(WeichenControlInterface):

    DEBUG = True

    def initialisation(self):
        if self.DEBUG:
            print("WeichenControlInterface " + "initialisation")

    def de_initialisation(self):
        if self.DEBUG:
            print("WeichenControlInterface " + "de_initialisation")

    def turnout_set_for_route(self, str_addr_low, str_addr_high, bol_color):
        if self.DEBUG:
            print("demo stelle Weiche " + str(bol_color))

    def turnout_free(self, str_addr_low, str_addr_high):
        if self.DEBUG:
            print("WeichenControlInterface " + "turnout_free")
