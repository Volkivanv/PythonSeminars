# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

lst = list(str(i) for i in range(0, len(list_1)) if min_number <= list_1[i] <= max_number)

# print(lst)
# print("\n".join(lst))

print("\n".join(list(str(i) for i in range(0, len(list_1)) if min_number <= list_1[i] <= max_number)))


# map(lambda x: print(x), lst)
#
# (print(item) for item in lst)
#
# for item in lst:
#     print(item)
