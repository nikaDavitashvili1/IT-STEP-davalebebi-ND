# davaleba 1
while True:
    try:
        ricxvi = int(input("write any number and i'll tell you it is even or odd: "))
        break
    except ValueError:
        print("please write a number and nothing else")

if ricxvi % 2 == 0:
    print("even")
else:
    print('odd')

# davaleba 2

momxmareblisTeqsti = str(input("chawere teqsti da tu shemdeg sityvebs - small, tall , middle - iqneba teqstshi, davbechdav: "))

small = str("small")
tall = str("tall")
middle = str("middle")

# elif-ebit rom damewera mxolod ert sityvas amobechdavda, amitom ramdenime ifs davwer.

if small in momxmareblisTeqsti:
    print(small)
if tall in momxmareblisTeqsti:
    print(tall)
if middle in momxmareblisTeqsti:
    print(middle)
if small or tall or middle not in momxmareblisTeqsti:
    print("None of these words have been written bro")

# davaleba 3

pirveliRicxvi = float(input("chamiwere nebismieri ricxvi: "))
meoreRicxvi = float(input("chamiwere meore ricxvi: "))
matematikuriOperatori = input("chamiwere matematikuri operatori shemdegi sityvebit - \nmultiplication division addition subtraction floor_division modulus exponentiation: ")

if matematikuriOperatori == "multiplication":
    print(pirveliRicxvi * meoreRicxvi)
elif matematikuriOperatori == "division":
    print(pirveliRicxvi / meoreRicxvi)
elif matematikuriOperatori == "addition":
    print(pirveliRicxvi + meoreRicxvi)
elif matematikuriOperatori == "subtraction":
    print(pirveliRicxvi - meoreRicxvi)
elif matematikuriOperatori == "floor_division":
    print(pirveliRicxvi // meoreRicxvi)
elif matematikuriOperatori == "modulus":
    print(pirveliRicxvi % meoreRicxvi)
elif matematikuriOperatori == "exponentiation":
    print(pirveliRicxvi ** meoreRicxvi)
else:
    print("Write exactly with the provided words please. Try again ")