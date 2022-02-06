import random
# a szavak:
szavak =  ["alma","fa","ablak","asztal","szék","körte","golyó","papucs","váza","szekrény","labda","szönyeg","pohár","üveg","lámpa","könvy","zokni","cipő","sál","nadrág","sapka","kesztyű","kabát","doboz","ceruza","hegyező","radir","táska"]
# változok / variables, listák
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
#________________________________________________________
# játék beállitások
print("Gondoltam egy szóra találd ki melyik az!")
print("10 szer probálkozhatsz alapból!")
print("Kettő segítséged van ha akarod használni ird be hogy: \"segitseg\"")
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
#________________________________________________________
# maga a program ciklusban
while True:
    bekeres = input("kérek egy betüt!\t")
    print("")
    if bekeres == "Lócaj_77":
        print("<<< Cheat code activated >>>")
        print(f"Gratulálok, eltaláltad! A szó amire gondoltam: {kivalaszt}")
        break
    if bekeres == "segitseg" and segitseg_szamlalo > 0:
        segitseg_szamlalo = segitseg_szamlalo - 1
        segi = random.choice(szeletelo)
        szeletelo.remove(segi)
        eltalalt.append(segi)
        print(f"Segítség aktiválva, a betű: \"{segi}\"\n")
        print(f"Az eltalált betük eddig: {eltalalt}\n")
        print(f"A rosz betük: {rossz}\n")
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
    tarolo = kereso
    if len(kereso) > 0:
        szeletelo.remove(tarolo[0])
        eltalalt.append(tarolo[0])
        print(f"Helyes! Ez a betü: \"{bekeres}\" szerepel a szóban\n")
        print(f"Az eltalált betük eddig: {eltalalt}\n")
        print(f"A rosz betük: {rossz}\n")
    elif len(kereso) == 0 and bekeres != "segitseg":
        elet = elet - 1
        rossz.append(bekeres)
        print(f"Nem, Ez a betű: \"{bekeres}\" NEM szerepel a szóban!\n")
        print(f"A jo betük eddig: {eltalalt}\n")
        print(f"A rosz betük: {rossz}\n")
    if elet == 0:
        print(f"Sajnálom elfogytak az életeid Vége a játéknak! A szó amire gondoltam: {kivalaszt}")
        print("<<< GAME OVER >>>")
        break
    if len(szeletelo) == 0:
        print(f"Gratulálok, eltaláltad! A szó amire gondoltam: {kivalaszt}")
        break
