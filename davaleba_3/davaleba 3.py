# # davaleba 1

while True:
    try:
        ricxvi = int(input("Chawere naturaluri ricxvi: "))
        break
    except ValueError:
        print("ricxvi chawere cifrebit")

while ricxvi > 0:
    print(ricxvi)
    ricxvi -= 1

# davaleba 2

total_sum = 0

while True:
    userInput = input("Chawere raime ricxvi an 'sum': ")
    if userInput == "sum":
        print("Chawerili dadebiti ricxvebis jamia:", total_sum)
        break

    try:
        number = float(userInput)
        if number >= 0:
            total_sum += number
    except ValueError:
        print("An ricxvi chawere an 'sum'. ")

# davaleba 3

import random

shemtxveviti_ricxvi = random.randint(1, 20)
cdebis_raodenoba = 10
while cdebis_raodenoba != 0:
    try:
        sheyvanili_ricxvi = int(input("gamoicani ricxvi: "))
        if sheyvanili_ricxvi == shemtxveviti_ricxvi:
            print("yochag, shen gamoicani ricxvi ", 10 - cdebis_raodenoba, "cdashi!")
            break
        elif sheyvanili_ricxvi > shemtxveviti_ricxvi:
            cdebis_raodenoba -= 1
            print("shesayvani ricxvi ufro naklebia. dagrcha ", cdebis_raodenoba, "mcdeloba")
        else:
            cdebis_raodenoba -= 1
            print("shesayvani ricxvi ufro metia. dagrcha ", cdebis_raodenoba, "mcdeloba")
    except ValueError:
        print("shieyvane mteli ricxvi cifrit")
