#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Osztalyokat mar ismerjuk korabbrol. Nezzuk, hogy nez ez ki Pythonban.
# Elavult jelolesmod:
# class Osztalyom:
#     pass
# Python3-ban azonban mar celszeru igy hasznalni, ez a gondolkodasmod
# ismeros lehet Java nyelvbol.
class Student(object):  # Wow, mibol oroklodunk?!
    # Osztaly attributumokat is felvehetunk, azonban ez kicsit eltero
    # mint pl. Java eseteben. Itt az osztaly adattagjait a konstruktorban
    # kell megadnunk. Na de hogy csinalunk konstruktort?
    # Eddig tanultaktol elteroen itt a konstruktornak mindig ugyanaz a neve,
    # ami nem az osztaly neve, hanem?!
    def __init__(self, name="Nincs nevem", age=12):
        # elso parameter az eddig ismert aktualis objektumra valo referencia
        # na akkor nezzuk, miket vegyunk fel egy diaknak
        self.name = name  # aktualis objektum vs. parameter neve
        self.age = age
        self._grades = list()  # ures lista (tomb)

    def add_grade(self, grade):
        self._grades.append(int(grade))

    def avg(self):
        sum_grades = 0
        for grade in self._grades:
            sum_grades += grade
        return sum_grades/len(self._grades)
        # return sum(self.grades) / len(self.grades)
        # Statisztikara bovebben:
        # https://docs.python.org/dev/library/statistics.html#statistics.mean

    def max_grade(self):
        return max(self._grades)

    def min_grade(self):
        return min(self._grades)

    # __dict__ mi lehet az?
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Class(object):
    def __init__(self):
        self._students = list()

    def new_student(self, student):
        if isinstance(student, Student):
            self._students.append(student)
        else:
            print("You can't do that")

    def avg(self):
        avgs = [student.avg() for student in self._students]
        return sum(avgs) / len(avgs)

    # Ismeros lehet a Java toString() metodusa
    # Ez ugyanaz, ha az objektumot kiiratjuk valahova, ennek a fuggvenynek
    # az eredmenyet kapjuk vissza.
    def __str__(self):
        return ("[Just a class, which consist of "
                "%d student(s).]" % len(self._students))

    # Ismeros lehet a Javabol, az equals metodus pontosan ugyanez.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __add__(self, other):
        if isinstance(other, Class):
            returned = Class()
            returned._students = self._students + other._students
            return returned


def main():
    # Hozzunk letre egy hallgatot
    cn = Student("Chuck Norris", 65)
    cn.add_grade(5)
    # cn.add_grade("sajt")
    cn.add_grade(2)
    print('Avg', cn.avg())
    print('Max. grade', cn.max_grade())
    print('Min. grade', cn.min_grade())

    js = Student('Jon Snow', 30)
    js.add_grade(1)
    js.add_grade(5)

    heroes = Class()
    heroes.new_student(cn)
    heroes.new_student(js)
    print('Class avg.', heroes.avg())
    print('Print the class variable', heroes)

    js2 = Student('Jon Snow', 30)
    js2.add_grade(1)
    js2.add_grade(5)

    heroes2 = Class()
    heroes2.new_student(cn)
    heroes2.new_student(js2)

    if heroes == heroes2:
        print('The 2 teams of heroes are equal.')
    else:
        print('The 2 teams of heroes are NOT equal.')

    heroes3 = heroes + heroes2
    print(heroes3)

if __name__ == '__main__':
    main()
