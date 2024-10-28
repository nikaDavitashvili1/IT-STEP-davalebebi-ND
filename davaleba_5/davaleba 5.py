# davaleba 1

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]
print("me-3 me-9 da me-14 elementebis jamia: ", mylist[2] + mylist[8] + mylist[13])

# davaleba 2

import random
randomList = []

for i in range(20):
    randomList.append(random.randint(0, 100))

newRandomList = []

for i in randomList:
    if i % 2 == 1:
        newRandomList.append(i)

# davalagot sia zrdadobit
for i in range(len(newRandomList) - 1):
    minIndex = i
    for j in range(i+1, len(newRandomList)):
        if newRandomList[minIndex] > newRandomList[j]:
            minIndex = j
    newRandomList[i], newRandomList[minIndex] = newRandomList[minIndex], newRandomList[i]

print("yvelaze didi da mcire kenti elementebis jamia: ", newRandomList[0] + newRandomList[-1])


# davaleba 3

my_llist = [43, '22', 12, 66, 210, ["hi"]]

for i in my_llist:
    if i == 210:
        print(my_llist.index(i))

my_llist.append("hello") # დაამატებს ბოლო ელემენტში ტექსტს "hello"
my_llist.pop(2) and print(my_llist) # წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს

my_llist_2 = []
for i in my_llist:
    my_llist_2.append(i)

my_llist_2.clear()

print(my_llist)
print(my_llist_2)

# davaleba 4

matrixList1 = [[1, 2, 3, 4], [4, 3, 2, 1], [0, 0, 0, 4], [0, 9, 0, 8]]
matrixList2 = [[1, 0, 7, 8], [0, 8, 6, 4], [5, 4, 2, 3], [7, 7, 7, 7]]

resultMatrix = []

for row in range(len(matrixList1)):
    resultRow = []
    for column in range(len(matrixList1[0])):
        elementSum = matrixList1[row][column] + matrixList2[row][column]
        resultRow.append(elementSum)

    resultMatrix.append(resultRow)

print("am ori matricis jamia: ", resultMatrix)

# davaleba 5

matrixBefore = [[1, 0, 3], [2, 5, 4], [8, 9, 7]]
matrixThen = [[], [], []]

rowIndex = 0
while rowIndex < len(matrixThen):
    newRow = matrixThen[rowIndex]
    for oldRow in matrixBefore:
        newRow.append(oldRow[rowIndex])
    rowIndex += 1

print("transponirebuli matrica: ", matrixThen)


# davaleba 6

compMatrix = []

for i in range(1, 5):
    row = []
    for j in range(1, 4):
        row.append(i)
        compMatrix.append(row)

print("list comprehensionit mighebuli matrica: ", compMatrix)
