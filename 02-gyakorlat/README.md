# 2. gyakorlat

## Az óra anyaga
- Lista (https://developers.google.com/edu/python/lists)
- Dictionary (https://developers.google.com/edu/python/dict-files)

## Feladatok
A feladatok a `03-exercises.py` fájlban elő vannak készítve.

### match_ends
Egy szövegeket tároló listát kap paraméterül a függvény.
A függvény számolja meg, hány olyan elem volt a listában, amik 2 karakteresek, vagy hosszabbak,
és az első és az utolsó betűje az adott szövegnek megegyezik.

### front_x
Egy szövegeket tároló listát kap paraméterül a függvény.
A függvény térjen vissza egy listával, amely legyen rendezve az alábbiak szerint:
ABC szerint legyenek rendezve benne a szöveget, annyival kiegészítve, hogy a lista elejére kerüljenek
azok a stringek, amelyek 'x' karakterrel kezdődnek.

Input: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
Output: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

### Téglalap
Írj egy osztályt, amely téglalapot reprezentál, annak oldalhosszait tárolja. Készíts neki konstruktort,
amely az oldalakat inicializálja, lehessen négyzetet is létrehozni. 
Készíts metódusokat a kerület és terület kiszámítására. Készíts hozzá main függvényt. Tárold a téglalapokat egy listában.
A listában lévő téglalapok területének és kerületének átlagát számítsd ki. 

### Receptkönyv
Készítsünk receptkönyvet. Ehhez szükségünk lesz egy Hozzávaló, Recept, Receptkönyv osztályra. 
A receptek egy adott mennyiségre szólnak (pl. 4 főre). Legyen egy olyan függvény, amely segítségével viszont tetszőleges számú
emberre alakítható a recept. Ezt a hozzávalók okos letárolásával érhetjük el. A receptnek legyen egy hozzávalók tömbje, amiben
tároljuk a recepteket. Ezen kívül tároljuk az elkészítési módot, időt, azt, és azt, hogy hány főre szól a recept

### Műsorújság
Készítsünk egy műsorújságot. Kell hozzá egy Műsor osztály, valamint a Műsorújság is. Egy műsornak van neve, korhatár-besorolása
(ezek a beérkező adattól függetlenül csak 12, 16, 18 lehet (tehát, ha 8 jön, akkor Műsor objektumban a korhatár-besorolás 12 lesz)),
kezdési és befejezési ideje.

A műsorújság osztályon belül legyen a csatorna neve és egy dictionary, amelynek kulcsai a hét napjai, értéke pedig egy lista a műsorokról. Ezek inicializálódjanak
a műsorújság létrehozásakor. Legyen egy új_műsor metódusa, ami egy napot, és egy műsort vár paraméterül. Csak akkor lehessen hozzáadni a műsorújsághoz,
ha az adott napon a már bent lévő műsorok közül az utolsó után kezdődik (tehát időrendben jönnek, és nincs átfedés). Lehessen
kérni statisztikát egy függvény segítségével, ami írjon ki mindenféle izgalmas dolgot a műsorújságról.

## Házi feladat

### Feldolgozni
- https://docs.python.org/3/library/enum.html - enumok Python nyelven
- https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
- https://docs.python.org/3/tutorial/classes.html