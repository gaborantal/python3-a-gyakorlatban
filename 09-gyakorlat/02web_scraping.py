#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


# requests - http://docs.python-requests.org/en/master/
# bs4 - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
def main():
    r = requests.get('https://twitter.com/taylorswift13')
    print('Response status code:', r.status_code)
    if r.status_code not in range(200, 299):
        print('Something bad happened!')
        return
    print(r.content)
    print(r.text.encode('utf-8'))  # Nem tudja megjeleniteni az osszes utf-8 karaktert
    # De ez sajnos nagyon keszekusza igy, mit tegyunk?
    # Lehet vegulis regexezgetni, de az nem tul idegbarat

    soup = BeautifulSoup(r.content, 'html.parser')
    all_tweet = soup.find_all('div', {'class': 'js-tweet-text-container'})
    print('Check out new tweets by Taylor Swift\n-------')
    for tweet in all_tweet:
        print(tweet.get_text().strip())
        print('-------')


if __name__ == '__main__':
    main()