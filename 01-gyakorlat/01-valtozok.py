"""
01-gyak: Python nyelv alapok, adattípusok
"""

"""
A Python a változót automatikusan azzal a típussal hozza létre, ami a legjobban megfelel az értéknek

Változónév-szabályok:
    * A változónév a (a  →  z , A  →  Z) betűk és a (0  →  9) számok sorozata, aminek mindig betűvel kell kezdődni.
    * Csak az ékezet nélküli betűk a megengedettek. A szóközök, a speciális karakterek, mint pl.: $, #, @, stb. nem használhatók.
      Kivétel a _ (aláhúzás).
    * A kis­ és nagybetűk különbözőnek számítanak. Figyelem : Jozsef, jozsef, JOZSEF különböző változók. Ügyeljünk erre ! 
"""

msg = "Hello!"
szoveg_1 = szoveg_2 = "Vilag"

var = 10
var_exists = 'var' in locals() or 'var' in globals()
print(var_exists)
del var
var_exists = 'var' in locals() or 'var' in globals()
print(var_exists)

valtozo_neve, valtozo_erteke = "PI", 3.14  # a tizedesjegyeket  tizedesponttal  választjuk el az egészrésztől

print(type(valtozo_neve))
print(type(valtozo_erteke))

print(msg, szoveg_1)
print(msg + " - " + szoveg_2)
print(valtozo_neve + " = " + str(valtozo_erteke)) # float -> str

# ********************************************* #

# aritmetikai muveletek
a = 12 + 24
b = 36 - 97
c = 6 * 7
d = 20 / 3 # !!!!!!!!!
e = 20 % 3
f = 4 + 5 * 7

"""
Ha egy műveletet vegyes típusú argumentumokkal hajtunk végre (egészekkel és valósokkal),
akkor a Python az operandusokat automatikusan valós típusúvá alakítja át mielőtt elvégzi a műveletet
"""
g = 4 * 2.5 / 3.3

h = 2 ** 4

print(a,b,c,d,e,f, g, h)
