#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv


def main():
    with open(os.path.join('data', 'students.csv'), 'r') as csv_file:
        student_reader = csv.DictReader(csv_file, delimiter=';')

        for student in student_reader:
            print('Neve:', student['nev'])
            # print(student)

    with open('names.csv', 'w', newline='') as csv_file:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Bacon', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

if __name__ == '__main__':
    main()
