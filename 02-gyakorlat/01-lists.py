#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pythonban nincs kulon, nativ tomb adatszerkezet
# Viszont van helyette a lista, amit hasznalhatunk
# Gyakorlatilag egy dinamikus tomb

# Referenciak vs ertek.
# Tuples vs. Lists

def main():
    list1 = []  # Ures lista (tomb) letrehozasa
    list2 = list()  # Ures lista (tomb) letrehozasa
    list3 = [2, 4, 6, 8, 10]  # Lista letrehozasa elemekkel

    # Egy lista barmilyen tipusu elemet tarolhat
    valtozo = 99
    list4 = [1, 2, 3, 1.1, 'cica', 3, valtozo, 123]

    # Hasznalatuk a mindenki altal ismert tombok hasznalataval megegyezik
    print('A list4 3. eleme:', list4[2])
    print(list4)

    # Elem hozzaadasa az append metodussal
    list4.append(-911)
    print('list4', list4)
    # negativ index eseten a lista vegetol vett elemet adja vissza
    print('list4 utolso eleme:', list4[-1])
    print('list4 utolso elotti eleme:', list4[-2])

    if 'cica' in list4:
        print('A cica benne van a list4-ben')
        print('A cica helye:', list4.index('cica'))

    # lista egy resze: tombindexek kozott kettosponttal megadjuk
    # az elso es az utolso elem indexet
    # a kezdo index benne van, de a befejezo mar nem
    print('list4 egy resze:', list4[2:5])  # 2, 3, 4. indexen levo elemek

    # Listak referencia szerint mukodnek
    list5 = list4
    print('list4', list4)
    print('list5', list5)
    list5.append(3)
    list5.append('kutya')
    print('list4', list4)
    print('list5', list5)

    # Ha megtalalja, eltavolitja az elso talalatot
    list5.remove(3)
    print('list4', list4)
    print('list5', list5)

    # count - Megszamolja, egy elem hanyszor van a listaban
    while list5.count(3) > 0:
        list5.remove(3)

    print('list4', list4)
    print('list5', list5)

    # Lista egy reszenek kimasolasa (a reszlista uj lista lesz!)
    list5 = list4[1:3]
    print('list5', list5)

    # Listak konkatenalasa
    list6 = list5 + list5
    print('list6', list6)
    list6 = list()
    list6.extend(list5)
    list6.extend(list5)
    print('list6', list6)

    # Lista sokszorozasa (hasonlo, mint a string eseteben)
    list7 = list5 * 5
    print('list7', list7)

    # Lista elemeinek osszefuzese egy stringge
    list8 = ['alma', 'korte', 'barack', 'cseresznye']
    print(list8)
    print(', '.join(list8))
    # Lista rendezese es visszaadasa
    print(sorted(list8))
    # Lista rendezese (NEM AD VISSZA SEMMIT)
    list8.sort(reverse=True)
    print(list8)

if __name__ == '__main__':
    main()
