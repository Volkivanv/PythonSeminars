# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3
# 2

lst = "1 2 3 2 3 3".split()
dct = {}

for item in lst:
    if item in dct:
        dct[item] += 1
    else:
        dct[item] = 1

n = 0
for item in dct:
    n += dct[item] * (dct[item] - 1) / 2

print(int(n))

nums = [1, 2, 3, 2, 3, 3, 3]
my_set = set(nums)
res = []
for el in my_set:
    res.append(nums.count(el) // 2)


print(sum([nums.count(el) // 2 for el in set(nums)]))

