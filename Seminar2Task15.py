# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint
N = int(input('Введите количество арбузов: '))
watermelons = []
for i in range(0, N):
    watermelons.append(randint(1,10))

print(watermelons)
print(f"Минимальный арбуз {min(watermelons)}")
print(f"Максимальный арбуз {max(watermelons)}")


lst = list(map(int, input("введите числа через пробел: ").split(" ")))
print(min(lst), max(lst))