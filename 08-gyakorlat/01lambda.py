#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce


def square(n):
    return n*n


def main():
    print('square(-3) =', square(-3))

    sq = lambda x: x*x
    print('sq(-3) =', sq(-3))

    mul = lambda x, y: x*y
    print('mult(6,5) =', mul(6, 5))

    # Altalanos szintaxis:
    # lambda parameterlista: kifejezes
    print_always = lambda *args: print(str(args))

    print_always(23, 123, 123, 12)
    print_always('Kiscica')
    print_always([0, 1, 2, 3, 4])
    print_always({'a': 12, 'b': 41})

    # Filterezes
    # Gyorsan hasznosan
    cars = []
    with open('cars.csv', 'r') as f:
        cars = f.readlines()
    cars = [car.strip().split(',') for car in cars]  # Autokat tartalmazo csv

    # Szurjuk ki a Toyotakat
    toyotas = list(filter(lambda c: 'toyota' in c[0].lower(), cars))
    print('All Toyota cars:', toyotas)

    # Map
    fahrenheits = [32, 65, 91, 105, 72, 55, 101, 77, 98]
    in_celsius = list(map(lambda f: (f-32)/1.8000, fahrenheits))
    print('All fahrenheits in celsius', in_celsius)

    # Reduce
    sum_temp = reduce(lambda x, y: x+y, in_celsius)
    print('Avarage temp.', sum_temp / len(in_celsius))

if __name__ == '__main__':
    main()
