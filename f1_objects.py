import random
from typing import List

import numpy as np


class Team:
    def __init__(self, drivers, constructor, captain="random"):

        self._drivers = drivers
        self._constructor = constructor

        if captain == "random":
            eligible_captains = [driver for driver in drivers if driver.price <= 20]
            self._captain = random.sample(eligible_captains, 1)[0]
        else:
            self._captain = captain

    @property
    def drivers(self):
        return self._drivers

    @property
    def captain(self):
        return self._captain

    @property
    def price(self):
        driver_prices = [driver.price for driver in self._drivers]
        return np.sum(driver_prices) + self._constructor.price

    @property
    def constructor(self):
        return self._constructor


class Driver:
    def __init__(self, name: str, constructor: str, price: float, teammate: str):

        self._name = name
        self._constructor = constructor
        self._price = price
        self._teammate = teammate

    @property
    def name(self):
        return self._name

    @property
    def constructor(self):
        return self._constructor

    @property
    def price(self):
        return self._price

    @property
    def teammate(self):
        return self._teammate


class Constructor:
    def __init__(self, name: str, price: float, drivers: List[str]):

        self._name = name
        self._price = price
        self._drivers = drivers

    @property
    def drivers(self):
        return self._drivers

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
