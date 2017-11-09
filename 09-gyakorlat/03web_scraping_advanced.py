#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from bs4 import BeautifulSoup
import requests


# requests - http://docs.python-requests.org/en/master/
# bs4 - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
def main():
    r = requests.get('http://kutyamutya.hu/kamujegyek.html')
    print('Response status code:', r.status_code)

    if r.status_code not in range(200, 299):
        print('Something bad happened!')
        return

    soup = BeautifulSoup(r.content, 'html.parser')
    tables = soup.find_all('table')
    for table in tables:  # Osszes <table>
        table_a = table.parent.find_previous_sibling("a")  # Table elotti egy szinten levo b-ket keressuk (Ez lesz a tablazat feletti cim)
        if table_a:  # Ha van ilyen (Lehet None)
            table_a = table_a.find_next_sibling("center")
            print(table_a.get_text())  # TODO(gabor_antal): regex datumra
        for row in table.find_all('tr'):
            # Easy way, last character is the grade
            #
            # row_text = row.get_text()
            # if 'Róka Kutya' in row_text:
            #     print(row_text)
            for row_cell in row.find_all('td'):
                cell_text = row_cell.get_text()
                if cell_text == 'Róka Kutya':
                    grade_data = row.find_all('td')[-2:]
                    if grade_data[0].get_text():
                        print('Róka Kutya got %s points' % grade_data[0].get_text())
                        print('Final grade: %s' % grade_data[1].get_text())
                        # TODO(gabor_antal): send email about this...

if __name__ == '__main__':
    main()
