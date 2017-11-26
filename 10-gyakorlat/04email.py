#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import emails


# from emails.template import JinjaTemplate as T


def main():
    message = emails.html(html=open(os.path.join('data', 'level.html')),
                          subject='Friday party',
                          mail_from=('Company Team', 'sztepython@gmail.com'))
    message.attach(data=open(os.path.join('data', 'pug.jpg'), 'rb'), filename='pug.jpg',
                   content_disposition='inline')

    r = message.send(to=('John Brown', 'sztepython@gmail.com'),
                     # render={'name': 'James Brown'},
                     smtp={'host': 'smtp.gmail.com',
                           'port': 465,
                           'ssl': True,
                           'user': 'sztepython',
                           'password': 'kiskutya'})

    if r.status_code not in [250, ]:
        print('Baj van')


if __name__ == '__main__':
    main()
