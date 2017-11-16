#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import os
from pathlib import Path
import platform
import shutil


def walk(dir_path):
    """Konyvtar bejarasa"""
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            path = os.path.join(root, file)
            # Barmit tehetunk a fajlokkal
            # print(path)
            if path.endswith('.py'):
                print('Found a python file', path)

if __name__ == "__main__":
    print('Current OS:', platform.system())
    cwd = os.getcwd()
    print('current_working_dir', cwd)
    print('cwd + ..\\', os.path.join(cwd, '..'))
    print('cwd + somedir/', os.path.join(cwd, 'somedir'))

    print('abspath of /', os.path.abspath('/'))
    print(r'cwd\..\..\somedir', os.path.join(cwd, '..', '..', 'somedir'))

    print(r'abspath cwd\..\..\somedir',
          os.path.abspath(os.path.join(cwd, '..', '..', 'somedir')))

    print('ENV', os.environ)

    print('Walk through cwd')
    walk(cwd)
    print('------')

    print('Current cwd', os.getcwd())
    os.chdir('..')
    print('Current cwd', os.getcwd())

    print('Base name of cwd:', os.path.basename(os.getcwd()))
    print('Relative path', os.path.relpath(os.getcwd()))
    print('Relative path of 10-gyakorlat/', os.path.relpath('10-gyakorlat'))
    print('Absolute path of this file', os.path.abspath('01os.py'))

    if not os.path.isdir('stuffs'):
        os.makedirs('stuffs/python-files')
        os.makedirs('stuffs/md-files')

    if os.path.exists('01os.py'):
        print('Letezik ez a fajl :) Mazli!')

    # Akutalis konyvtarban mukodik, os.chdir() ahova szukseges
    all_py = glob.glob('*/*.py')
    print('All Python files', all_py)

    # Python 3 valtozat, Path osztaly hasznalataval
    # Itt mar nem kell abba a konyvtarba lepni, arra hivatkozo objektumot
    # hozunk letre! :)
    all_md = Path('.').glob('*/*.md')  # Generator objektumot ad vissza

    # Egy Path-okat tartalmazo generator kifejezest ad vissza.
    # Ezt listava alakitjuk
    # A listaban Path objektumok vannak.
    # Ezeket osszemappeljuk az str() fuggvennyel.
    # Ebbol egy map object lesz, ezt listava alakitjuk
    all_md = list(map(str, list(all_md)))
    print('All markdown files', all_md)

    for py_file in all_py:
        shutil.copy(py_file, os.path.join('stuffs', 'python-files'))

    for md_file in all_md:
        shutil.copy2(md_file, os.path.join('stuffs', 'md-files'))  # Bogaras kod
        # TODO(gaborantal): bugfix

    shutil.make_archive('archive', 'zip', os.path.join('stuffs', 'md-files'))
    shutil.copyfile('README.md', os.path.join('stuffs', 'md-files', 'index.md'))

    # copytree
    delete = False
    if delete:
        shutil.rmtree('stuffs')
