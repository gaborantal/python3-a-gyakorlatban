#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys


"""
print("This is the name of the script: " + sys.argv[0])
print("Number of arguments: " + str(len(sys.argv)))
print(sys.argv)
"""

def arg_parser():
    parser = argparse.ArgumentParser(prog="argv", description="Progi leirasa")
    parser.add_argument("-a", "--arg1",
                        required=True,
                        help="Ez az arg1 leirasa")

    parser.add_argument("-b", "--arg2",
                        default="default_arg2",
                        help="Ez az arg2 leirasa")

    parser.add_argument("-c",
                        choices=["asd", "fgh", "ijk"],
                        default="fgh",
                        help="Ez az arg3 leirasa")

    args = parser.parse_args()
    arg1 = args.arg1
    arg2 = args.arg2
    arg3 = args.c
    return arg1, arg2, arg3

arg1, arg2, arg3 = arg_parser()
print(arg1)
print(arg2)
print(arg3)