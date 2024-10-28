# davaleba 1

squared_numbers = set()

for i in range(1,11):
    squared_numbers.add(i**2)

print(squared_numbers)

# davaleba 2
letter_set = set()

for i in input("chawere rac ginda: "):
    letter_set.add(i)

print(letter_set)

# davaleba 3
tuple1 = (1, 2, 4, 4, 7, 8)
tuple2 = (1, 3, 3, 4, 5, 6, 7)
combined_tuple = []
duplicated_values = []

for i in tuple1+tuple2:
    if i not in combined_tuple:
        combined_tuple.append(i)
print(combined_tuple)

for i in tuple1 and tuple2:
    if i in tuple1 and i in tuple2:
        duplicated_values.append(i)

print(duplicated_values)

# davaleba 4

first_tuple = (1, 2, 3, 4, 5)
second_tuple = (first_tuple[-1],) + first_tuple[1:-1] + (first_tuple[0],)
print(second_tuple)

# davaleba 5

input_tuple = (1, (2, 3), (4, (5, 6)))
new_list = list(input_tuple)
result = ()

while new_list:
    item = new_list.pop(0)
    if isinstance(item, tuple):
        new_list = list(item) + new_list
    else:
        result += (item,)

print(result)

# davaleba 6

set1 = {1, 2, 3, 4}
set2 = {"a", "b", "c", "d"}
combined_set = set()

for i in set1:
    for j in set2:
        combined_set.add((i, j))

print(combined_set)