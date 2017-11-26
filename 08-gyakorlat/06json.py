#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def main():
    s = '{"nev": "Nagy Zsolt", "email": "nagy@zsolt.hu"}'

    e1 = json.loads(s, encoding='utf8')
    print('Az ember dictionary:', e1)
    print('Nev:', e1['nev'])
    print('Email cim:', e1['email'])

    # ha nem vagyunk benne biztosak, hogy van adott attributum
    # hasznaljuk a get() metodust (lasd: dict..)
    print('Kedvenc autoja:', e1.get('kedvenc_auto'))

    if not e1.get('kedvenc_auto'):  # None false-nak ertekelodik ki
        e1['kedvenc_auto'] = 'BMW'

    print('Frissitett ember', e1)
    print(json.dumps(e1))

    e2 = {'nev': 'Eros Pista', 'email': 'eros@pista.hu'}
    everyone = [e1, e2]

    with open(os.path.join('data', 'students.json'), 'w') as fp:
        json.dump(everyone, fp)

    with open(os.path.join('data', 'cars.json'), 'r') as fp:
        cars_from_json = json.load(fp)

    cars_from_json = cars_from_json['data']

    print('Cars from JSON', cars_from_json)

if __name__ == '__main__':
    main()
