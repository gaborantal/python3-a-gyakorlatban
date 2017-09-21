#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Lista gyakorlatilag dinamikus tomb, indexelve van 0-tol kezdodoen
# Nyilvan lehet olyan, hogy a hagyomanyos egesz -> barmi lekepezes helyett
# Jobban jonne, ha az index egy szoveg lenne (pl.: JSON)
# Nagy szerencse, hogy ezt is megoldhatjuk eleg egyszeruen


def main():
    osztaly_letszamok = {}
    dict2 = dict()
    dict3 = {
        'name': 'Robert Paulson',
        'kor': 30,
        'ferfi': True
    }

    print("A neve %(name)s, %(kor)d eves es ferfi? %(ferfi)s" % dict3)

    osztaly_letszamok['1a'] = 23
    osztaly_letszamok['2b'] = 35
    osztaly_letszamok['3a'] = 25
    osztaly_letszamok['1b'] = 19

    print('Osztaly letszamok:', osztaly_letszamok)
    print('Jelenleg %d osztalynak tudjuk a letszamat' % len(osztaly_letszamok))
    print('Osztalyok, amik letszamat tudjuk:', osztaly_letszamok.keys())
    print('A 3.a letszama', osztaly_letszamok['3a'], 'fo')
    # print('Az 5.zs letszama', osztaly_letszamok['5zs'], 'fo')
    # Ajjaj, a kozvetlen hivatkozas nem biztos, hogy mindig jo
    # ha nem vagyunk benne biztosak, hogy adott elem letezik, erdemes a get()
    # metodust hasznalni
    # Ez visszater a letszammal, ha letezik az elem, kulonben None-nal
    print('Az 5.zs letszama', osztaly_letszamok.get('5zs'), 'fo')

    if '1b' in osztaly_letszamok:  # if '1b' in osztaly_letszamok.keys():
        print('Az 1b osztaly letszamat tudjuk!')

    if 25 in osztaly_letszamok.values():  # ertekek kozott keres
        print('Van 25 fos osztaly!')

    # Dictionary szetbontasa egy tuple listava. tuple -> (kulcs, ertek)
    # [('3a', 25), ('2b', 35), ('1a', 23), ('1b', 19)]
    print(osztaly_letszamok.items())

    # Bejaras
    for kulcs, ertek in osztaly_letszamok.items():
        print('A(z)', kulcs, ' osztalyba', ertek, ' fo jar.')

    for kulcs in osztaly_letszamok:
        print(kulcs, '=>', osztaly_letszamok[kulcs])

    osztaly_letszamok['7k'] = 50
    print(osztaly_letszamok)
    # Jaj, a 7k megse letezik! Most mi legyen?
    del osztaly_letszamok['7k']
    print(osztaly_letszamok)

if __name__ == '__main__':
    main()
