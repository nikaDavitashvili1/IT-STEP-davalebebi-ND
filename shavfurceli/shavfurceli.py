# import re
#
# text = 'gamarjoba, chemi saxelia nika'
#
# pattern = r'[aeiou]'
# matches = re.findall(pattern, text)
#
# print(matches)
#
# def sheamowme_validuroba(a, b, c):
#     if (a + b <= c) or (a + c <= b) or (b + c <= a):
#         return False
#     else:
#         return True
#
#
# while True:
#     try:
#         a = int(input("chawere a gverdis sigrdze: "))
#         b = int(input("chawere b gverdis sigrdze: "))
#         c = int(input("chawere c gverdis sigrdze: "))
#         break
#     except ValueError:
#         print("chawere ricxvit da ara asoebit")
#
# if sheamowme_validuroba(a, b, c):
#     print("arsebobs aseti samkutxedi")
# else:
#     print("ar arsebobs aseti samkutxedi")
# from os.path import exists


# tupl = (1, 2, 3)
# tupl2 = (1, 23, [6, 3])
# tupl += tupl2
# print(tupl)
# tupl2[-1].append("hola")
# print(tupl2)


# new_tuple = ("first", "second", "third", "fourth", "fifth", "sixth")
# first, second, *others, lastbeforelast, last = new_tuple
# print(new_tuple)
# print(first)
# print(second)
# print(others)
# print(last)
# print(lastbeforelast)
#
# for o in enumerate(new_tuple, start=1):
#     print(o)

# print(new_tuple.count("first"))
# print(new_tuple.index("first"))

# set1 = {}
# print(type(set1))
# set2 = set()
# print(type(set2))
# set3 = {1, 2, 3, 4, 3, "hola"}
# print(set3)
# set2.update(new_tuple)
# print(set2)
#
# print(set2)
#
# set4 = {1, 3, 5}
# print(set4)
# set4.add("a")
# print(set4)
# print(set4.pop())
# set4.update("b")
# print(set4)

# globaluri diqti
# funqcia romelic moitxovs saxels da gvars
# sheinaxet globalur dictshi

# global_dict = {"first_name": "", "last_name": ""}
#
# momxmareblis_saxeli = input("chawere saxeli: ")
# momxmareblis_gvari = input("chawere gvari: ")
#
#
# def Input():
#     global momxmareblis_saxeli
#     global momxmareblis_gvari
#     global_dict["first_name"].__add__(momxmareblis_saxeli)
#     global_dict["last_name"].__add__(momxmareblis_gvari)
#     return global_dict
#
# print(global_dict)

# global_dict = {}
# global_list = []
#
# def create_profile(firstname, lastname, **kwargs):
#     global global_dict
#     global global_list
#
#     global_dict.setdefault("firstname", firstname)
#     global_dict.setdefault("lastname", lastname)
#
#     global_list.append(global_dict)
#     print(global_dict)
#
# create_profile("<NAME>", "<NAME>")
# create_profile("jasjad", "bakjfa")
# create_profile("okjm", "bakiuhbnmjfa")

# def nth_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
#
# n = 7
# result = nth_fibonacci(n)
# print(result)

