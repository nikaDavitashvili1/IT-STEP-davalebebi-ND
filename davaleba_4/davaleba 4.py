# davaleba 1

momxmareblisTeqsti = str.upper(input("Chawere teqsti da getyvi palindromia tu ara: "))

if momxmareblisTeqsti == momxmareblisTeqsti[::-1]:
    print("sheyvanili teqsti aris palindromi")
else:
    print("sheyvanili teqsti ar aris palindromi")

# davaleba 2

userInput = input("sheiyvane teqsti da dagibechdav ascii cods: ")

for i in userInput:
    print(ord(i))