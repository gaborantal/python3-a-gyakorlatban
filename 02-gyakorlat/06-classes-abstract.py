#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


# Az ital egy altalanos fogalom, de az a baj, hogy ugyanugy letre lehet hozni,
# mint barmely mas osztalyt. Viszont a price() metodusnak igy nincs ertelme,
# es nem is lenne jo, ha letre lehetne hozni egy italt.
# Tegyuk absztraktta!
# Ehhez a Python ABC modulja fog kelleni. ABC = Abstract Base Class
# Python 3.4+ verziokban eleg csak az ABC osztalybol szarmazni, korabbi
# valtozatokban viszont be kell allitani az osztaly metaclassjat az ABCMetara
# Python 3.0+
#   class Drink(metaclass=ABCMeta):
# Python 2.0+
#   class Drink:
#       __metaclass__ = ABCMeta
# https://stackoverflow.com/a/13646263/5738367
class Drink(ABC):
    def __init__(self, dl=0.0):
        self.dl = dl

    @abstractmethod
    def price(self):
        """
        :return: price of the drink
        """
        pass


class CarbonatedDrink(Drink):
    def __init__(self, dl=0.0, bubbles=100):
        super(CarbonatedDrink, self).__init__(dl)
        self.bubbles = bubbles

    def __str__(self):
        return 'CarbonatedDrink [dl=%f, bubbles=%d]' % (self.dl, self.bubbles)

    def price(self):
        return self.dl * 50 + ((100-self.bubbles)/5)


def main():
    # x = Drink()
    # print('Price of x', x.price())

    sth = CarbonatedDrink(3, 100)
    print(sth)
    print(sth.price())

if __name__ == '__main__':
    main()
