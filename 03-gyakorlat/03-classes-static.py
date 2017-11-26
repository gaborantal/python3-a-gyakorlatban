#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Car(object):
    # Minden olyan valtozo, ami osztaly szinten van megosztva
    # Azaz az adott osztaly minden peldanyara egy es ugyanaz valtozo lesz
    # A peldanyok osztoznak rajta
    wheels = 4  # Minden autonak negy kereke van
    _count = 0

    def __init__(self, brand='Toyota', model='Supra 1978'):
        self.brand = brand
        self.model = model
        Car._count += 1

    # Itt nincs elso self parameter, sem semmi egyeb. Amit parameternek kiirom
    # Azt varom, nincs trukkozes, staightforward.
    @staticmethod
    def print_count(placeholder='Number of cars: %d'):
        print(placeholder % Car._count)

    # Hasonlo, mint a staticmethod, de kicsit megis mas lesz
    # A classmethod megkapja implicit modon az osztalyt, mint parametert
    # Persze hasznalhatjuk ugy, ahogy eddig, de a trukkozes majd mindjart jon
    @classmethod
    def print_number_of_cars(cls, placeholder='Number of cars: %d'):
        print(placeholder % Car._count)
        print('Class of method:', str(cls.__name__))

    # A trukk pedig a kovetkezo: mivel a konstruktorunk ket szoveget var
    # ezert, ha egy szoveggel hivom meg, azt fogja hinni, hogy az az auto tipusa
    # pedig siman lehet, hogy nem. Es itt jon a classmethod segitsegul
    # Jellemzoen alternativ konstruktorokra szoktuk oket hasznalni
    # Na azt hogy? Hat igy
    # https://stackoverflow.com/a/1950927/5738367
    @classmethod
    def from_primitive(cls, primitive_str):
        # kapunk egy szoveget, amiben a kocsi markaja es tipusa el van valasztva
        # mondjuk pontosvesszovel, es abbol akarunk peldanyt letrehozni.
        splitted = primitive_str.split(';')
        if len(splitted) == 2:
            # Letrehozunk egy peldanyt
            instance = cls()
            instance.brand = splitted[0]
            instance.model = splitted[1]
            return instance
        else:
            print('Nem sikerult jol megadni; itt egy auto')
            return cls()


class FlyingCar(Car):
    pass


def main():
    lada = Car('Lada', '2107')
    niva = Car('Lada', 'Niva')
    supra = Car()

    print('Lada 2107 wheels:', lada.wheels)
    print('Lada Niva wheels:', niva.wheels)
    print('Supra wheels:', supra.wheels)
    print('Car class wheel attribute', Car.wheels)

    niva.wheels = 8  # Csak a peldanyban szereplo ertek valtozik meg
    print('-- Niva has 8 wheels now')
    print('Lada 2107 wheels:', lada.wheels)
    print('Lada Niva wheels:', niva.wheels)
    print('Supra wheels:', supra.wheels)
    print('Car class wheel attribute', Car.wheels)

    Car.wheels = 7
    print('-- Every car has 7 wheels now')
    print('Lada 2107 wheels:', lada.wheels)
    print('Lada Niva wheels:', niva.wheels)  # Except Niva
    print('Supra wheels:', supra.wheels)
    print('Car class wheel attribute', Car.wheels)

    # Ez a metodus sokkal inkabb az osztalyhoz tartozik, mintsem
    # egyes peldanyokhoz, hiszen a peldanyok adatai nem szuksegesek
    # a fuggveny futtatasahoz, csak minden peldanyban elerheto osztalyvaltozot
    # hasznal es a fuggveny parametereit.
    lada.print_count()  # ne
    niva.print_count()  # ne
    Car.print_count('We have %d cars.')

    lada.print_number_of_cars()

    flying = FlyingCar()
    flying.print_number_of_cars()

    corolla = Car.from_primitive('Toyota;Corolla 2005')
    print('Added model:', corolla.model)

if __name__ == '__main__':
    main()
