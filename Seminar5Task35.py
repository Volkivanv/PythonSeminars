# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_prime_rec(n, max_div):
    if max_div == 1:
        return 'Yes'
    if n % max_div == 0:
        return 'No'
    return is_prime_rec(n, max_div - 1)


k = int(input("введите число: "))


print(is_prime_rec(k, round(k ** 0.5)))
