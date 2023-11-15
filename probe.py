import math

print("Something")
coins = [0, 1, 0, 1, 1, 0, 1, 1, 0]

# Введите ваше решение ниже


print(min(coins.count(0), coins.count(1)))

s = 12
p = 27

x1 = round((s - (s**2 - 4*p)**0.5)/2)
x2 = round((s + (s**2 - 4*p)**0.5)/2)

print(x1, x2)
