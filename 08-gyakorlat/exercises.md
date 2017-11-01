# Feladatok

## Maximális elem kiválasztása a reduce használatával
Lásd: exercises.py fájl

## Kocsi adatok
0. A feladat a `cars.csv` beolvasása a csv.DictReader segítségével. A beolvasott objektumokból készítsünk `Car` objektumokat. 
Ehhez hozzuk létre a `Car` osztályt. A `rendszamok.txt` fájlban találunk az autókhoz rendszámokat. A fájl beolvasása után
egységesítsük a rendszámokat BBB-000 formátumú rendszámmá, így "tegyük fel" egy kocsira. Mindegyik rendszámot adjuk hozzá
valamelyik autóhoz (az egyszerûség kedvéért érdemes sorban haladni. Az így elkészült adathalmazt:

1. Mentsük ki json fájlba. 
2. Csak a kocsi típusa+rendszám adatokat mentsük ki a csv.DictWriter segítségével!
3. Szûrjük az autókat: tároljuk el egy listában a 96 kW teljesítményû autókat (1 lóerõ = 0.745699872 kilowatt)
4. Válasszuk ki a listából azt az autót, amelyik a leggyorsabban gyorsul fel 100 km/h-ra, a reduce() segítségével.
5. Készítsünk egy listát a map() segítségével, amelyben legyen benne, hogy az egyes autók hány évesek (jelenlegi év - gyártás)

## Email validátor 
Készítsünk egy e-mail cím validátor függvényt. Térjen vissza igazzal, ha e-mail címet adtunk neki paraméterben, különben pedig hamissal.