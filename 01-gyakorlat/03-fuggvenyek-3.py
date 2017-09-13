
def szamologep(a, b):

    def _osszead():
        return a+b

    def _kivon():
        return a-b

    def _oszt():
        return a/b

    def _szoroz():
        return a*b

    return _osszead(), _kivon(), _oszt(), _szoroz()

eredmenyek = szamologep(12, 20)
print(eredmenyek)
print(eredmenyek[0], eredmenyek[3])
print(eredmenyek[1:3])