import random
szavak =  ["tank","almafa","villámháború","körte","bojler"]
hosz = len(szavak[0])
elet = 9
tipp = 0
kivalaszt = random.choice(szavak)
eltalalt = []
szeletelo = []
for betu in kivalaszt:
    szeletelo.append(betu)

print("Gondoltam egy szóra találd ki melyik az!")
print("10 szer probálkozhatsz alapból!")
kerdes = input("Akarod e megváltoztatni az életed számát? (i/n)\t")
if kerdes == "i":
  try:
    elet2  = int(input("Mennyi életed lenne?\t"))
  except:
    print("Számot kértem töki!")
    print("Ha már ilyen vicces hangulatban vagy akkor kevesebb életed lesz! :)")
    elet2 = 3
elif kerdes != "n" or kerdes != "i":
  print("Nincs ilyen opció, akkor ennyi életed lesz: 10")
  elet2 = 10
else:
  elet2 = 10
print(f"Ennyi probálkozásod van akkor alapból: {elet2}")
print("________________________________________\n")

while True:
    bekeres = input("kérek egy betüt!\t")
    kereso = [szo for szo in szeletelo if bekeres == szo]
    if elet == 0 or elet2 == 0:
        print(f"Sajnálom elfogytak az életeid Vége a játéknak! A szó amire gondoltam: {kivalaszt}")
        print("<<< GAME OVER >>>")
        break
    if len(kereso) > 0:
        tipp = tipp + 1
        szeletelo.remove(kereso[0])
        eltalalt.append(kereso[0])
        print(f"Helyes! Ez a betü: \"{bekeres}\" szerepel a szóban")
        print(f"Az eltalált betük eddig: {eltalalt}")
    else:
        elet = elet - 1
        elet2 = elet2 - 1
        print(f"Nem, Ez a betű: \"{bekeres}\" NEM szerepel a szóban!")
        print(f"A jo betük eddig: {eltalalt}")
    if tipp == len(szeletelo):
        print(f"Gratulálok, eltaláltad! A szó amire gondoltam: {kivalaszt}")
        break

