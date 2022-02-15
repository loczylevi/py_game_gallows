"""2.4 Feladat
Fejlesszük tovább a 2.3 programot úgy, hogy a program egy listában tároljon öt darab szót, és abból véletlenszerűen válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.
"""

import random
print("Gondoltam egy tárgyra találd ki!\n Mnidig egy betüt adhatsz meg!\n alapból 10 életed van hacsak,\n meg akarod változtatni!")
try:
  elet = int(input("Mennyi probálkozással szeretnél játszani?\t"))
except:
  print("Számot kértem uram!")
  elet = 10
jo_tipp = []
rossz_tipp = []
szavak = ["kalap","ablak","cumi","váza","tank"]
veletlen = random.choice(szavak)
szeletelo = [betu for betu in veletlen]
if 0 > elet:
    print(f"Sajnálom {elet} életed nem lehet,\n 0-nál nagyobb értéket kellet volna megadnod!")
    elet = 10
while True:
  if len(szeletelo) == 0:
      print(f"Gratulálok! Kitaláltad amire gondoltam! \n A szó amire gondoltam: {veletlen}")
      break
  if elet == 0:
    print(f"Sajnálom elfogytak a probálkozásaid!\n A szó amire gondoltam: {veletlen}")
    print("<<< GAME OVER >>>")
    break
  bekeres = input("Kérek egy betüt!\t")
  if bekeres == "":
    print("<<< Program vége >>>")
    break
  kereso = [betu for betu in veletlen if      bekeres == betu]
  if len(kereso) > 0:
    jo_tipp.append(bekeres)
    try:
      szeletelo.remove(bekeres)
    except:
      jo_tipp.remove(bekeres)
      elet = elet - 1
    print(f"Ez a betü: \"{bekeres}\" szerepel a változóban!\n A szó: {bekeres}\n")
    print(f"Jó tippek: {', '.join(jo_tipp)}")
    print(f"Rossz tippek: {', '.join(rossz_tipp)}")
    print(f"Ennyi életed van még: {elet}")
  else:
    elet = elet - 1
    rossz_tipp.append(bekeres)
    print(f"Ez a betü: \"{bekeres}\" NEM szerepel a változóban!\n A szó: {bekeres}\n")
    print(f"Jó tippek: {', '.join(jo_tipp)}")
    print(f"Rossz tippek: {', '.join(rossz_tipp)}")
    print(f"Ennyi életed van még: {elet}")

    
