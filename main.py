import random
szavak =  ["tank","almafa","villámháború","körte","bojler"]
hosz = len(szavak[0])
elet = 9
tipp = 0
kvalaszt = random.choice(szavak)
eltalalt = []
szeletelo = []
for betu in szavak[0]:
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
    elet2 = 2
elif kerdes != "n" or kerdes != "i":
  print("Nincs ilyen opció, akkor ennyi életed lesz: 10")
  elet2 = 9
else:
  elet2 = 9
print(f"Ennyi probálkozásod van akkor alapból: {elet2+1}")
print("________________________________________\n")

while True:
    bekeres = input("kerek egy betut ")
    kereso = [szo for szo in szeletelo if bekeres == szo]
    if elet == 0:
        print(f"Sajnálom elfogytak az életeid Vége a játéknak! A szó amire gondoltam: {szavak[0]}")
        print("<<< GAME OVER >>>")
        break
    if len(kereso) > 0:
        tipp = tipp + 1
        szeletelo.remove(kereso[0])
        eltalalt.append(kereso[0])
        print(f"Ez a betü: \"{bekeres}\" szerepel a szóban")
        print(f"jo valaszok: {eltalalt}")
    else:
        elet = elet - 1
        print(f"Ez a betü: \"{bekeres}\" NEM szerepel a szóban")
        print(f"jo valaszok: {eltalalt}")
    if tipp == hosz:
        print("nyertél!!")
        break
    if elet == 0:
        print(f"élet egyenlő: {elet} GAME OVER")
        break

