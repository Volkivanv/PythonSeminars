# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
#
# Функция не должна ничего выводить, только возвращать значение.

def f(base, power):
    if power == 0:
        return 1
    return base * f(base, power - 1)


a = 3
b = 5
print(f(a, b))
