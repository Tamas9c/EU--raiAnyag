import collections


with open("EUcsatlakozas.txt" , "r" , encoding='latin2') as f:
    lista = list() 
    for sor in f:
        lista.append(sor.strip().split(";"))
        
        
#3.feladat
print( f"3.feladat: EU tagállamainak száma : {len(lista)} db")


#4.feladat
szamlaló = 0
for orszag, datum in lista:
    if datum[0:4] == "2007":
        szamlaló =szamlaló + 1
print( f"4.feladat: 2007-ben {szamlaló} csatlakozott.")

#5.feladat
for ország ,datum in lista:
    if ország == "Magyarország":
        print( f"5.feladat: Magyarország csatlakozásának dátuma: {datum} ")

#6.feladat
számláló = 0
for orszag, datum in lista:
    if datum[5:7] == "05":
        számláló = számláló + 1
if számláló > 0 :
    print( f"6.feladat: Májusban volt csatlakozás ")
else:
    print( f"6.feladat: Májusban nem volt csatlakozás ")

#7.feladat
datum0 = ""
for orszag, datum in lista:
    if datum0 < datum:
        datum0 = datum
        orszag0 = orszag
print( f"7.feladat: Legutoljára  csatlakozott  ország: {orszag0}")

#8.feladat
cnt = collections.Counter()
for orszag, datum in lista:
    cnt[datum[0:4]] += 1 
print(f"8.feladat: Statisztika")
for év, darab in cnt.items():
    print(f"    {év} - {darab} ország")