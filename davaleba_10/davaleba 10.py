# from functools import reduce
#
# # davaleba 1
#
# lst1 = [1, 2, 3, 4, 5]
# lst2 = ["a", "b", "c", "d", "e"]
#
# result = [item for item in zip(lst1, lst2)]
# print(result)
#
# # davaleba 2
#
# all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# even_numbers = filter(lambda x: x % 2 == 0, all_nums)
# print(list(even_numbers))
#
# # davaleba 3
#
# random_numbers = [-1, 1, -4, 4, -65, -1092, 100, 1000, -1283]
# positive_numbers = filter(lambda x: x >= 0, random_numbers)
# print(list(positive_numbers))
#
# # davaleba 4
#
# list_of_strings = ["Hello", "There", "nan", "peRfecT", "wow", "deed", "MaDAm"]
#
# check_if_palindrome = lambda string: string.lower() == string[::-1].lower()
# result = list(filter(check_if_palindrome, list_of_strings))
# print(result)
#
# # davaleba 5
#
# list_of_numbers = ["hmm"]
#
# while True:
#     try:
#         result = reduce(lambda x, y: x * y, list_of_numbers)
#         break
#     except TypeError:
#         result = "invalid input"
#
# print(result)


list_zipper = lambda list1, list2: list(zip(list1, list2))

print(list_zipper([1,2,3],[4,5,6]))

onlyEvens = lambda lst: [x for x in lst if x % 2 == 0]
print(onlyEvens([1,2,3,4,5,6,7,8,9]))