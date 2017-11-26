#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def main():
    letter = lambda: random.choice('abcdefghijklmnopqrstuvwxyz')

    with open('rendszamok.txt', 'w') as fp:
        for i in range(392):
            b = letter()
            b += letter()
            b += letter()
            num = str(random.randint(0, 9))
            num += str(random.randint(0, 9))
            num += str(random.randint(0, 9))

            seged = random.random()
            if seged < 0.3:
                fp.write("%s -%s" % (b, num))
            elif 0.3 <= seged < 0.6:
                fp.write("%s%s" % (b, num))
            else:
                fp.write("%s-%s" % (b, num))
            fp.write('\n')

if __name__ == '__main__':
    main()
