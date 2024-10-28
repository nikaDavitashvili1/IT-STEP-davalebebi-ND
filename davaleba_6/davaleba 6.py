# davaleba 1

userInput = str(input("Chawere rame winadadeba da me dagitvli romeli sityva ramdenjer meordeba: "))

dict1 = {}

for word in userInput.split():
    if word not in dict1:
        dict1[word] = 1
        continue
    if word in dict1:
        dict1[word] += 1

print(dict1)

# davaleba 2

ricxvi1 = float(input("chawere pirveli ricxvi: "))
ricxvi2 = float(input("chawere meore ricxvi: "))
matematikuriOperatori = input("chawere matematikuri operatori: ")

calculator_dict = {}

calculator_dict.update({"+": ricxvi1 + ricxvi2})
calculator_dict.update({"-": ricxvi1 - ricxvi2})
calculator_dict.update({"*": ricxvi1 * ricxvi2})
calculator_dict.update({"/": ricxvi1 / ricxvi2})
calculator_dict.update({"%": ricxvi1 % ricxvi2})
calculator_dict.update({"**": ricxvi1 ** ricxvi2})
calculator_dict.update({"//": ricxvi1 // ricxvi2})

print(calculator_dict.get(matematikuriOperatori))

# davaleba 3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squareDict = {x : x**2 for x in lst}
print(squareDict)

# davaleba 4

tanamshromlebisDict = {"departamenti":
                          {"marketing":
                              {"chief":
                                  {"saxeli":"Ani", "gvari":"Darsimelia", "asaki":25, "xelfasi": 12000},
                                "upper manager":
                                    {"saxeli":"Nika", "gvari":"Berulava", "asaki":30, "xelfasi": 6000},
                                "intern":
                                   {"saxeli":"Luka", "gvari":"Kekelidze", "asaki":18, "xelfasi": 1200}
                                },
                           "management":
                               {"chief":
                                   {"saxeli": "Zurab", "gvari": "Balanchivadze", "asaki": 50, "xelfasi": 10000},
                                "upper manager":
                                    {"saxeli": "Bacho", "gvari": "Bartia", "asaki": 40, "xelfasi": 5000},
                                "intern":
                                    {"saxeli": "Merab", "gvari": "Zhvania", "asaki": 20, "xelfasi": 2500}
                                   },
                           "finances":
                               {"chief":
                                   {"saxeli": "Cerdric", "gvari": "Drigory", "asaki": 27, "xelfasi": 14000},
                                "upper manager":
                                    {"saxeli": "Archil", "gvari": "Napetvradze", "asaki": 28, "xelfasi": 7000},
                                "intern":
                                    {"saxeli": "Nino", "gvari": "Abesadze", "asaki": 19, "xelfasi": 2000}
                                   },
                           "it":
                               {"chief":
                                   {"saxeli": "Mariam", "gvari": "Ratchvelishvili", "asaki": 32, "xelfasi": 99999},
                                "upper manager":
                                    {"saxeli": "Zviad", "gvari": "Zviadauri", "asaki": 40, "xelfasi": 55555},
                                "intern":
                                    {"saxeli": "Lado", "gvari": "Chikovani", "asaki": 20, "xelfasi": 11111}
                                   }
                              }
                         }


markSalary = 0
managSalary = 0
finanSalary = 0
itSalary = 0
count = 0

for key, value in tanamshromlebisDict.items():
    for key1, value1 in value.items():
        if key1 == "finances":
            count = 0
            for key2, value2 in value1.items():
                for key3, value3 in value2.items():
                    if key3 == "xelfasi":
                        count += 1
                        finanSalary += value3

for key, value in tanamshromlebisDict.items():
    for key1, value1 in value.items():
        if key1 == "management":
            count = 0
            for key2, value2 in value1.items():
                for key3, value3 in value2.items():
                    if key3 == "xelfasi":
                        count += 1
                        managSalary += value3


for key, value in tanamshromlebisDict.items():
    for key1, value1 in value.items():
        if key1 == "it":
            count = 0
            for key2, value2 in value1.items():
                for key3, value3 in value2.items():
                    if key3 == "xelfasi":
                        count += 1
                        itSalary += value3


for key, value in tanamshromlebisDict.items():
    for key1, value1 in value.items():
        if key1 == "marketing":
            count = 0
            for key2, value2 in value1.items():
                for key3, value3 in value2.items():
                    if key3 == "xelfasi":
                        count += 1
                        markSalary += value3


print(managSalary/count)
print(finanSalary/count)
print(itSalary/count)
print(markSalary/count)
