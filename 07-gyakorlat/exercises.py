#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import time

# TDD Calculator kozosen

# Keszits teszteket az alabbi fuggvenyekhez:
# - ellenorizzuk, hogy meg lett-e hivva a function
# - ellenorizzuk, hogy a time.sleep() meg lett-e hivva 60-nal
# - termeszetesen ne varjunk egy percet! :)
def sleep_and_execute(func):
    time.sleep(60)
    func()

# - ellenorizzuk, hogy a recv 4096-tal lett-e meghivva
# - keszitsunk valid tesztet es invalid tesztet is
# - ellenorizzuk, hogy dobodik-e kivetel
def read(sock):
    data = sock.recv(4096)
    if data == '':
        raise socket.error('socket closed')
    return data

