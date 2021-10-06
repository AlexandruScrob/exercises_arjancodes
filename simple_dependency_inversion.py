from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print('LightBulb: tuned on')

    def turn_off(self):
        print('LightBulb: tuned off')


class Fan(Switchable):
    def turn_on(self):
        print('Fan: tuned on')

    def turn_off(self):
        print('Fan: tuned off')


class ElectricPowerSwitch:

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False

        else:
            self.client.turn_on()
            self.on = True


lw = LightBulb()
switch = ElectricPowerSwitch(lw)
switch.press()
switch.press()
