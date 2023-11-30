# Задача №37. Общее обсуждение
# 5 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse_print(lst):
    if len(lst) == 1:
        print(lst[0])
    else:
        print(lst[-1], end=' ')
        reverse_print(lst[:-1])


def input_list(length):
    if length == 1:
        return [int(input("введите число"))]
    else:
        return input_list(length - 1) + [int(input("введите число"))]


l = int(input("введите длину списка: "))
lst = input_list(l)
print(lst)

reverse_print(lst)
