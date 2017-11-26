# 3. gyakorlat

## Téglalap
Írj egy osztályt, amely téglalapot reprezentál, annak oldalhosszait tárolja. Készíts neki konstruktort,
amely az oldalakat inicializálja, lehessen négyzetet is létrehozni. 
Készíts metódusokat a kerület és terület kiszámítására. Készíts hozzá main függvényt. Tárold a téglalapokat egy listában.
A listában lévő téglalapok területének és kerületének átlagát számítsd ki. 

## Receptkönyv
Készítsünk receptkönyvet. Ehhez szükségünk lesz egy Hozzávaló, Recept, Receptkönyv osztályra. 
A receptek egy adott mennyiségre szólnak (pl. 4 főre). Legyen egy olyan függvény, amely segítségével viszont tetszőleges számú
emberre alakítható a recept. Ezt a hozzávalók okos letárolásával érhetjük el. A receptnek legyen egy hozzávalók tömbje, amiben
tároljuk a recepteket. Ezen kívül tároljuk az elkészítési módot, időt, azt, és azt, hogy hány főre szól a recept

## Műsorújság
Készítsünk egy műsorújságot. Kell hozzá egy Műsor osztály, valamint a Műsorújság is. Egy műsornak van neve, korhatár-besorolása
(ezek a beérkező adattól függetlenül csak 12, 16, 18 lehet (tehát, ha 8 jön, akkor Műsor objektumban a korhatár-besorolás 12 lesz)),
kezdési és befejezési ideje.

A műsorújság osztályon belül legyen a csatorna neve és egy dictionary, amelynek kulcsai a hét napjai, értéke pedig egy lista a műsorokról. Ezek inicializálódjanak
a műsorújság létrehozásakor. Legyen egy új_műsor metódusa, ami egy napot, és egy műsort vár paraméterül. Csak akkor lehessen hozzáadni a műsorújsághoz,
ha az adott napon a már bent lévő műsorok közül az utolsó után kezdődik (tehát időrendben jönnek, és nincs átfedés). Lehessen
kérni statisztikát egy függvény segítségével, ami írjon ki mindenféle izgalmas dolgot a műsorújságról.
