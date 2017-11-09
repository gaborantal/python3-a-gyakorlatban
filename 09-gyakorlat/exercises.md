# Feladatok

## 03web_scraping_advanced befejezése
Maradt néhány TODO, ezeket be lehet fejezni.

## Táblázatfeldolgozó PIMP
A fenti fájlban lévõ táblázat feldolgozása, az adatok lementése könnyen kezelhetõ CSV formátumban. Az adatokból különbözõ statisztika
kinyerése, hány hallgató kapott egyest, kettest, hármast, négyest, ötöst. Az eredmények megjelenítése egy webszerveren. Az oldalon lévõ
link hatására frissítse a tartalmat, számolja újra a statisztikát.

## Web2MD
Például a http://www.inf.u-szeged.hu/~antal/ oldal (de bármi lehet, akár wiki cikk, stb) kimentése MD fomrátumban (vagy lehet txt is):

- A fõoldalon lévõ linkek mindegyikére is hívjuk meg az átalakítót.
- Nem kell, hogy tökéletes legyen: elég ha bizonyos elemekre mûködik (cím, div, a, p, span, stb, bármi).
- Képeket, rövidítsen a tinyurl.py használatával.

## Online fájlszerkesztõ
Egy elõre elkészített CSV fájl online szerkesztése, bárki által (vagy akár autentikáció után).

- Egy webes API-n keresztül lehessen kommunikálni: /read - a fájl akutális állapota, kicsit megszépítve, vagy akár JSON-nel (GET kérés)
- Szerkesztés, a tördelés segítségével, pl. egyszerre egy szót cserélhetünk: /modify/SOR/SZÓ_SZÁMA (mondjuk pontosvesszõvel tördeljük). (POST kérés)
- A szerkesztésrõl jöjjön válasz: melyik szót cseréltük le mire.

## WebZipDownloader
Például a http://www.inf.u-szeged.hu/~antal/?p=prog2 oldalon lévõ összes link bejárása, és ha .zip a kiterjesztése, akkor töltse le:

- Ehhez használd a urllib.request.urlretrieve függvényt. Bõvebben: https://stackoverflow.com/a/7244263/5738367, https://docs.python.org/dev/library/urllib.request.html#urllib.request.urlretrieve
- Letöltés után használd az shutils.make_archive függvényt, hogy az összes zipbõl egy nagy zip fájlt készíts! https://docs.python.org/3/library/shutil.html#shutil.make_archive
