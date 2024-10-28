# დავალება 1
# ჩავაწერინოთ მომხმარებლებს რიცხვები და დავუწეროთ ჯამი. თუ მთელ რიცხვებს არ დაწერს მივცეთ თავიდან ჩაწერის საშუალება
while True:
    try:
        x1 = int(input("Chawere pirveli shesakrebi: "))
        x2 = int(input("Chawere meore shesakrebi: "))
        x3 = int(input("Chawere mesame shesakrebi: "))
        break
    except ValueError:
        print("mteli ricxvi unda chawero, torem programa ar imushavebs")

print("am sami ricxvis jamia: ", x1 + x2 + x3)

# დავალება 2

while True:
    try:
        kubis_Gverdis_Sigrdze = int(input("chawere kubis gverdis sigrdze: "))
        break
    except ValueError:
        print("kubis gverdis sigrdze mteli ricxvi unda iyos")


cubeSurface = (kubis_Gverdis_Sigrdze ** 2) * 6
cubeVolume = kubis_Gverdis_Sigrdze ** 3

print("kubis zedapiris fartobia: ", cubeSurface)
print("kubis moculobaa: ", cubeVolume)

# დავალება 3

while True:
    try:
        monitorisFasi = float(input("chawere monitoris fasi: "))
        sistemuriBlokisFasi = float(input("chawere sistemuri blokis fasi: "))
        klaviaturisFasi = float(input("chawere klaviaturis fasi: "))
        mausisFasi = float(input("chawere mausis fasi: "))
        break
    except ValueError:
        print("fasebi chawere ricxvebit")

print("aseti kompiuteri dagijdebat ", monitorisFasi+sistemuriBlokisFasi+klaviaturisFasi+mausisFasi, "₾")