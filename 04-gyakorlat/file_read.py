#!/usr/bin/python

import argparse


def input_arg_parser():
    parser = argparse.ArgumentParser(prog="file_read", description="File read")
    parser.add_argument("-i", "--input", required=True, help="input file")
    args = parser.parse_args()
    input_file = args.input
    return input_file


def file_methods(file_name):
    F = open(file_name, "r")
    print(dir(F))

# beolvassa egy str-be a fajl tartalmat
def read_1(file_name):
    F = open(file_name, "r")
    line = F.read()
    print(line) # kiirja a teljes szoveget
    print(line[1]) # kiirja a masodik karaktert
    F.close()


def read_2(file_name):
    F = open(file_name, "r")
    line = F.readline() # beolvassa a fajl elso sorat
    print(line) # kiirja az elso sort
    print(line[1]) #kiirja a masodik karaktert
    line = F.readline() # beolvassa a kovetkezo sort
    print(line) # kiirja a kovetkezo sort
    F.close()

def read_3():
    F = open(input_arg_parser(), "r")
    lines = F.readlines() # beolvassa az osszes sort
    print(lines) # kiirja a sorokat tartalmazo listat
    print(lines[1]) # kiirja a masodik sort
    F.close()

# read_3
def read_4():
    with open(input_arg_parser(), 'r') as infile:
        for line in infile:
            print(line)

file_methods(input_arg_parser())
#read_1(input_arg_parser())
#read_2(input_arg_parser())
#read_3()
read_4()
