import random
# a szavak:
szavak =  ["alma","fa","ablak","asztal","szék","körte","golyó","papucs","váza","szekrény","labda","szönyeg","pohár","üveg","lámpa","könvy","zokni","cipő","sál","nadrág","sapka","kesztyű","kabát","doboz","ceruza","hegyező","radir","táska"]
# változok / variables, listák
cuccmokok = ["%","+","*","_","-","="]
for szam in range(0,9):
    cuccmokok.append(str(szam))
ismeretlen = ""
elet = 10
kivalaszt = random.choice(szavak)
eltalalt = []
szeletelo = []
rossz = []
tarolo = ""
segitseg_szamlalo = 2
figy = 0
for betu in kivalaszt:
    szeletelo.append(betu)
meddig = len(szeletelo)
for sor in range(len(kivalaszt)):
    k = random.choice(cuccmokok)
    cuccmokok.remove(k)
    ismeretlen = ismeretlen + k

#________________________________________________________
# játék beállitások
print("Gondoltam egy szóra találd ki melyik az!")
print("10 szer probálkozhatsz alapból!")
print("Kettő segítséged van ha akarod használni ird be hogy: \"segitseg\"")
print("A program mutatja az adott betű helyiértékét is!\n(Az ismeretlen betük helyén számok és egyébb karakterek állnak. Pl: *,+,%,9)")
kerdes = input("Akarod e megváltoztatni az életed számát? (i/n)\t")
if kerdes == "i":
    try:
        elet  = int(input("Mennyi életed lenne?\t"))
    except:
        print("Számot kértem töki!")
        print("Ha már ilyen vicces hangulatban vagy akkor kevesebb életed lesz! :)")
        elet = 3
elif kerdes == "n":
    elet = 10
elif kerdes != "i" or kerdes != "n":
    print("Nincs ilyen opció, akkor ennyi életed lesz: 10")
    elet = 10
print(f"Ennyi probálkozásod van akkor alapból: {elet}")
print("________________________________________\n")
print(f"A szó hosszúsága: {meddig}")
if 0 > elet:
    print(f"Sajnálom {elet} életed nem lehet,\n 0-nál nagyobb értéket kellet volna megadnod!")
    elet = 10
#________________________________________________________
# maga a program ciklusban
while True:
    if elet == 0:
        print(f"Sajnálom elfogytak az életeid Vége a játéknak! A szó amire gondoltam: {kivalaszt}")
        print("<<< GAME OVER >>>")
        break
    if len(szeletelo) == 0:
        print(f"Gratulálok, eltaláltad! A szó amire gondoltam: {kivalaszt}")
        break
    bekeres = input("kérek egy betüt!\t")
    print("")
    if len(bekeres) > 1 and bekeres != "segitseg" and bekeres != "Lócaj_77":
      print(f"Egy karaktert kértem! Nem {len(bekeres)}!")
    if bekeres.isnumeric() == True:
      print("Szöveget kértem nem számot!")
      bekeres = int(bekeres)
    if bekeres == "Lócaj_77":
        print("<<< Cheat code activated >>>")
        print(f"Gratulálok, eltaláltad! A szó amire gondoltam: {kivalaszt}")
        break
    if bekeres == "segitseg" and segitseg_szamlalo > 0:
        segitseg_szamlalo = segitseg_szamlalo - 1
        segi = random.choice(szeletelo)
        szeletelo.remove(segi)
        eltalalt.append(segi)
        for betu in eltalalt:
          hol = kivalaszt.index(betu)
          ismeretlen = ismeretlen.replace(ismeretlen[hol], betu)
        print(f"Segítség aktiválva, a betű: \"{segi}\"\n")
        print(f"A kitalált betük helyiértéke: {ismeretlen}\n________________________________________\n")
        print(f"Az eltalált betük eddig: {', '.join(eltalalt)}\n")
        print(f"A rosz betük: {', '.join(rossz)}\n")
    if bekeres == "segitseg" and segitseg_szamlalo == 0:
        print(f"Figy{figy} Segítséget csak kétszer használhatod! :)")
        figy = figy + 1
        if figy == 4:
            print("Szándékos csalási folyamatért büntetés jár!!!\n -3 élet")
            elet = elet - 3
        elif figy == 8:
            print("Túlságosan sokszor szerettél volna segítséget haszálni!\n Ezért a kitartó probálkozásaidnak hála a játékod véget ért!\n")
            elet = 0
    # a program kulcs sora:
    kereso = [szo for szo in szeletelo if bekeres == szo and bekeres != "segitseg"]
    if len(kereso) > 0:
      for _ in range(len(kereso)):
        szeletelo.remove(bekeres)
        eltalalt.append(bekeres)
      for betu in eltalalt:
        hol = kivalaszt.index(betu)
        ismeretlen = ismeretlen.replace(ismeretlen[hol], betu)
      print(f"Helyes! Ez a betü: \"{bekeres}\" szerepel a szóban\n")
      print(f"A kitalált betük helyiértéke: {ismeretlen}\n________________________________________\n")
      print(f"Az eltalált betük eddig: {', '.join(eltalalt)}\n")
      print(f"A rosz betük: {', '.join(rossz)}\n")
    elif len(kereso) == 0 and bekeres != "segitseg" and len(bekeres) == 1:
        elet = elet - 1
        rossz.append(bekeres)
        print(f"Nem, Ez a betű: \"{bekeres}\" NEM szerepel a szóban!\n")
        print(f" A kitalált betük helyiértéke: {ismeretlen}\n________________________________________\n")
        print(f"A jo betük eddig: {', '.join(eltalalt)}\n")
        print(f"A rosz betük: {', '.join(rossz)}\n")
