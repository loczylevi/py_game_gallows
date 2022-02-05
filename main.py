import random
szavak =  ["tank","almafa","villámháború","körte","bojler"]
hosz = len(szavak[0])
elet = 3
tipp = 0
eltalalt = []
szeletelo = []
for betu in szavak[0]:
    szeletelo.append(betu)
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

