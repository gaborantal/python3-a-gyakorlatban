# Python virtuális környezet

Szóval a Python egyik legnagyobb erőssége, hogy rengeteg minden el van hozzá készítve, akár a standard függvénykönyvtár részeként, akár letölthető
külső függvénykönyvtárként. Ez eddig világos, de vajon hogy működni a valóságban? Megírjuk a kötelező programot, amihez egy csomó ilyen külső dolgot használunk. És utána?! Felírjuk egy lapra, hogy miket szedtünk le, és reméljük, hogy az oktató is azt a verziót használja, és nem lesz ebből gond? Nem teljesen, sokkal okosabb megoldás lesz.

Erre megoldás lesz a `virtualenv` használata, amely segítségével virtuális, szeparált környezeteket hozhatunk létre, és amiket azon belül telepítünk, azt később le tudjuk majd kérni, ezt a listát a feladat beadásakor mellékeljük, és akkor boldogság van, hiszen az oktató is le tudja majd pontosan azokat a verziókat szedni, amiket a program írásakor használtunk.

Oké, vágjunk bele akkor. Mi kell ehhez? Ehhez és még sok egyéb csomag telepítéséhez a pip csomagkezelő fog kelleni.

## pip 

A pip egy csomagkezelő rendszer, amely operációs rendszertől függetlenül használható mindegyiken, és sok hasznos dolgot tud. Alapvetően, Python 2.7.9 (a kettes változatoknál) és Python 3.4 (a hármas változatoknál) verziótól kezdődően tartalmazza a pip csomagkezelőt. Ha esetleg nincs, akkor le lehet tölteni a [hivatalos oldalról](https://pip.pypa.io/en/stable/installing/).

Akkor telepítsünk vele fel egy csomagot, például a `virtualenv`-et. Ehhez parancssorba be kell pötyögnünk a `pip install virtualenv` parancsot (adminisztrátorként). Ez a legutóbbi stabil kiadást fogja jelenteni, de ha nem elégszünk meg ezzel, és mindenképpen a legfrissebb fejlesztői változatra van szükségünk, a pip segítségével bármit telepíthetünk egy bármilyen git verziókövetőből, ebben az esetben a `pip install https://github.com/pypa/virtualenv/tarball/develop` parancsot kell kiadnunk.

Hozzunk létre egy virtuális környezetet:

`virtualenv beadando`

Ezzel elkészült a virtuális környezet a projektünkhöz, mostmár csak aktiválnunk kellene 

- Linux:
`source beadando/bin/activate`

- Windows:
`beadando\Scripts\activate`

Az aktív környezetből kilépni a `deactivate` paranccsal tudunk. Amíg nem lépünk ki, minden telepítés a virtuális környezetben történik majd.

Például telepítünk valamit:
`pip install bármi`

Amennyiben minden szükséges külső függvénykönyvtárat telepítettünk a beadandóhoz, valahogy rögzíteni kéne, hogy az oktató is pontosan azokat a verziókat telepíthesse:
Ehhez a `pip freeze` parancsot kell használnunk, ez a stdout-ra kiírja az összes, környezetben telepített függvénykönyvtárat. Irányítsuk fájlba

`pip freeze > requirements.txt`
A `requirements.txt` fájlt általában a projekt gyökerébe tesszük, ezt felismeri a PyCharm is, és sok más IDE is.

Ha kapunk valahonnan egy projektet, ahol ilyet látunk, nem kell megijedni, nem kézzel telepítünk mindent, a pip ebben is segít:

`pip install -r requirements.txt`

Ez mindent úgy telepít fel, ahogy az a requirements.txt fájlban rögzítve van. Ezt általában célszerű egy virtuális környezetbe tenni.

Ha pedig egy virtuális környezetre nincs szükségünk, csak kitöröljük: `rm -rf beadando/`
