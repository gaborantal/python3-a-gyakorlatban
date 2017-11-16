#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import re
import requests


# https://github.com/django/django/blob/master/django/utils/text.py
def name(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)


def download(url, name):
    resp = requests.get(url)
    with codecs.open(name+'.html', "w", "utf-8") as fp:
        fp.write(resp.text)
    return resp.status_code

if __name__ == '__main__':
    urls = ['http://inf.u-szeged.hu/',
            'https://www.ebay.com/',
            'http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://europe.wsj.com/',
            'http://www.bbc.co.uk/',
            'https://docs.python.org/3/library/concurrent.futures.html']

    start_time = datetime.now()
    with ThreadPoolExecutor(max_workers=1) as executor:
        for url in urls:
            future = executor.submit(download, url, name(url))
            # print(future.result())
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
