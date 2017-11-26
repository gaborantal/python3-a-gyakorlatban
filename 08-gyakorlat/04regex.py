#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

RENDSZAM_REGEX = r'\b([A-Z]{3}) ?-? ?([0-9]{3})\b'
RENDSZAM_REGEX = re.compile(RENDSZAM_REGEX, re.IGNORECASE)  # Miert?


# https://docs.python.org/2/library/re.html
# https://regex101.com/
def main():
    # Alapveto match
    pattern = r'Zombie Elvis Found'
    s = 'Oh my god! Zombie Elvis found! The newspaper is named ' \
        '"Liberty Cock". It depicts the headline, along with a black and ' \
        'white photograph of late Elvis Presley\'s face'
    print('-- Elso proba')
    if re.match(pattern, s):
        print('Megvan a zombi Elvis!')
    else:
        print('Huh! Nincs meg vilagvege.')

    print('-- Masodik proba')
    # flags -> megadas bitenkenti vagy segitsegevel
    # re.M = multiline, re.I = ignorecase
    if re.match(pattern, s, re.IGNORECASE):
        print('Megvan a zombi Elvis!')
    else:
        print('Huh! Nincs meg vilagvege.')

    # Match: String elejen probal meg illeszteni
    # Search: Barhol a stringben
    print('-- Harmadik proba')
    if re.search(pattern, s, re.IGNORECASE):
        print('Megvan a zombi Elvis!')
    else:
        print('Huh! Nincs meg vilagvege.')

    print('-- Rendszamok')
    with open(os.path.join('data', 'rendszamok.txt'), 'r') as rendszam_file:
        rendszamok = rendszam_file.read()
    rendszamok = rendszamok.split('\n')

    for rendszam in rendszamok:
        siker = RENDSZAM_REGEX.match(rendszam)
        if siker:
            print("A rendszam: %s-%s" % (siker.group(1), siker.group(2)))
        else:
            print('A "%s" nem valid rendszam!' % rendszam)


if __name__ == '__main__':
    main()
