# 1. Swallow exceptions
A feladat egy olyan context manager/dekorátor elkészítése, ami elnyeli a megadott típusú kivételeket

    with swallow_exceptions([ZeroDivisionError]):
            1 / 0
    Nullaval valo osztas lenyelve

# 2. Better debug
A feladat egy dekorátor elkészítése, ami rendes debug hibaüzenetet ír ki: időpont, meghívott metódus neve, argumentumok, visszatérési érték, esetleg kivétel.

    @debug
    def division(n):
        return n / 0

    @debug
    def another_division(n):
        return n / 2

    >>> another_division(10)
    another_division parameterek:  (10,) {}
    visszateresi ertek: 5

    >>> division(10)
    division got (10,) {}
    raised: integer division or modulo by zero
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero

# 3. YOLO Cache
A feladat egy olyan context manager/dekorátor elkészítése, amely csökkenti a CPU terhelését, mégpedig cache-elés segítségével.
Ehhez tárolja el a beérkező paramétereket, és a függvény által kiszámolt értéket. Ha legközelebb érkeznek olyan paraméterek, melyek
már korábban voltak, és rögzítettük a visszatérési értékét, akkor ne hívja meg a függvényt, hanem a cace-ben tárolt értékkel térjen vissza,
hiszen nem érünk rá örökké! `exercises.py`

Pluszpontért: Egy 'timeout' paraméter a cache-hez, hogy meddig maradjanak benne a tárolt értékek, ha nincsenek használva.


# 4. Deprecated dekorátor
A feladat egy olyan context dekorátor elkészítése, ami figyelmezteti a felhasználót, hogy elavult függvényt használt. Csak az első függvényhasználatkor szóljon.

# 5. flatten generátor
A feladat egy olyan generátor függvény írása, amelynek bejárható paramétereket adva transzparensen visszaadja
az egymást követő bejárható dolgok elemei.

    for i in flatten(range(3), range(3, 5)):
        print(i)
    
    > 0 1 2 3 4

# 3. 
A feladat egy olyan context manager/dekorátor elkészítése,

# 3. 
A feladat egy olyan context manager/dekorátor elkészítése,