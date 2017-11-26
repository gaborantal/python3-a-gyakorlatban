#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib.request

# Innen (csak nem mukodik): https://github.com/daxeel/TinyURL-Python


def shorten(long_url, alias):
    URL = "http://tinyurl.com/create.php?source=indexpage&url=" + long_url + "&submit=Make+TinyURL%21&alias=" + alias
    response = urllib.request.urlopen(URL)
    soup = BeautifulSoup(response, 'html.parser')
    check_error = soup.p.b.string
    if "The custom alias" in check_error:
        return "Alias you have selected is already used by someone else."
    else:
        return soup.find_all('div', {'class': 'indent'})[1].b.string


if __name__ == '__main__':
    print(shorten("www.chemista.in", "ckgw9285jztf"))
