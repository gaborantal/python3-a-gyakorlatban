#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class Student(object):
    def __init__(self, nev=None, email=None, kedvenc_auto=None):
        self.nev = nev
        self.email = email
        self.kedvenc_auto = kedvenc_auto

    def to_json(self):
        return json.dumps(self.__dict__)

    def say_hello(self):
        print('Hello! A nevem {0}, az email cimem: {1}, '
              'a kedvenc autom pedig {2}.'.format(self.nev,
                                                  self.email,
                                                  self.kedvenc_auto))

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    @classmethod
    def from_json_dict(cls, json_dict):
        return cls(**json_dict)


def main():
    with open('students.json', 'r') as fp:
        raw_data = json.load(fp)
    students = [Student.from_json_dict(x) for x in raw_data]

    for s in students:
        s.say_hello()

if __name__ == '__main__':
    main()
