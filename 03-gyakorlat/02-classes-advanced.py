#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Cake(object):
    def __init__(self, slices=10, flavour='chocolate'):
        self._slices = slices
        self._flavour = flavour

    @property
    def slices(self):
        print('# Accessed to Cake#_slices via slices property')
        return self._slices

    @slices.setter
    def slices(self, new_slices):
        if new_slices > 0:
            print('# New number of slices is ok, updated')
            self._slices = new_slices
        else:
            print('# Cannot update number of slices, invalid value was',
                  new_slices)

    def __str__(self):
        return '[Cake, slices=%d, flavour=%s]' % (self._slices, self._flavour)


# Egyszeru oroklodes, oroklunk ugyan, de se nem egeszitjuk ki, se nem veszunk
# fel uj metodusokat, adattagokat. Van ez igy...
class RottenCake(Cake):
    pass


class BirthdayCake(Cake):
    def __init__(self, slices=10, flavour='chocolate', years=20):
        # os konstruktoranak inicializalasa
        # https://docs.python.org/3/library/functions.html#super
        # https://stackoverflow.com/a/33469090/5738367
        super(BirthdayCake, self).__init__(slices, flavour)
        # Python 3 felett megtehetjuk csak igy:
        # super().__init__(slices, flavour)
        self.years = years

    def __str__(self):  # override
        return 'BirthdayCake[years=%d, %s]' % (
            self.years, super(BirthdayCake, self).__str__())


def main():
    choco = Cake(slices=16)
    print(choco)
    print(choco.slices)  # hozzaferes a propertyhez
    choco.slices = 10  # valtoztatunk a propertyn keresztul
    print(choco)
    choco.slices = -10  # invalid modositas a property erteken
    print(choco)

    rotten = RottenCake(flavour='bad', slices=8)
    print('Rotten cake', rotten)
    del rotten  # torolhetjuk is oket, elvesztjuk a referenciat
    # print(rotten)  # hibas sor a fenti torles miatt

    banana = BirthdayCake(flavour='banana', years=24)
    print(banana)
    print('birthday cake is cake?', isinstance(banana, Cake))
    print('type of banana is subclass of Cake?', issubclass(type(banana), Cake))
    banana.slices = -10  # oroklodes


if __name__ == '__main__':
    main()
