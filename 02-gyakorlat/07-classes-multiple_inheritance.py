#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, dl=0.0):
        self.dl = dl

    @abstractmethod
    def price(self):
        """
        :return: price of the drink
        """
        pass


class Wine(Drink):
    def __init__(self, dl=0.0, winery='Danko', alcohol=0.12):
        super().__init__(dl=dl)
        self.winery = winery
        self.alcohol = alcohol
        print('- Wine constructor')


    def price(self):
        return self.dl * 250

    def __str__(self):
        return 'Wine[dl=%f, winery=%s, alcohol=%f]' % (self.dl,
                                                       self.winery,
                                                       self.alcohol)


class Cola(Drink):
    def __init__(self, dl=0.0, brand='Coca Cola', sugar_free=False):
        super().__init__(dl=dl)
        self.brand = brand
        self.sugar_free = sugar_free
        print('- Cola constructor')

    def price(self):
        return self.dl * 70

    def __str__(self):
        return "Cola[brand=%s, dl=%f, sugar_free=%s" % (self.brand,
                                                        self.dl,
                                                        self.sugar_free)


# Diamond problem, MRO
# http://www.python-course.eu/python3_multiple_inheritance.php
# https://stackoverflow.com/a/26927718/5738367
# https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path
class MagicPotion(Cola, Wine):

    def __init__(self, dl=1.0, brand='?', winery='?', sfree=False):
        half = dl/2.0
        Wine.__init__(self, dl=half, winery=winery, alcohol=0.08)
        Cola.__init__(self, dl=half, brand=brand, sugar_free=sfree)

    def __str__(self):
        return "Magic Potion[cola=%s, wine=%s]" % (Cola.__str__(self),
                                                   Wine.__str__(self))

    def price(self):
        return 2*self.dl*125


def main():
    redwine = Wine(winery='Kekfrankos', alcohol=0.11)
    print(redwine)

    cc = Cola(dl=4)
    print(cc)
    print('----')
    potion = MagicPotion(5)
    print(potion)

    print(potion.price())

if __name__ == '__main__':
    main()
