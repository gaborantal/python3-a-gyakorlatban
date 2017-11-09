#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from bs4 import BeautifulSoup
import requests

VIEWS = 0


# requests - http://docs.python-requests.org/en/master/
# bs4 - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
def main():
    global VIEWS
    r = requests.get('https://www.youtube.com/watch?v=wIft-t-MQuE')
    print('Response status code:', r.status_code)

    if r.status_code not in range(200, 299):
        print('Something bad happened!')
        return
    # Tipp: Ne csak a bongeszobol nezegesd a kodot, hanem toltsd le, a requests
    # mit lat belole. A letoltott tartalmat ird ki egy fajlba, abbol dolgozz!
    with open('taylor_swift1.html.txt', 'w') as fp:
        fp.write(r.content.decode('utf-8'))

    # Ezt akar eleg egyszer megcsinalni, amig keszitjuk/teszteljuk a progit,
    # es akkor meg veletlen sem fog ugy kinezni a dolog, mint egy DDoS attack :)
    # Ha ez megvan, akar eleg csak beolvasni a fajlbol a tartalmat
    soup = BeautifulSoup(r.content, 'html.parser')
    watch_count_results = soup.find_all('div', {'class': 'watch-view-count'})

    watch_count = watch_count_results[0].get_text()  # Tudjuk, hogy egy talalat lesz csak.
    print('Watch count:', watch_count)  # Ezt nem tujduk szamma konvertalni, ajjaj

    tmp = watch_count.split(' ')
    tmp = tmp[:-1]  # Lista
    print(str(tmp))  # Ajjaj
    tmp = ''.join(tmp)  # Lista -> String
    tmp = tmp.replace(u"\xa0", "")  # string replace

    current_count = int(tmp)
    if current_count > VIEWS:
        print('New viewers, updating!')
        VIEWS = current_count

if __name__ == '__main__':
    for i in range(10):
        main()
        time.sleep(10)
