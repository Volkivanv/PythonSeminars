list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))

print(list_1)

data = "3 5 2 9 9"
data = list(map(int, data.split()))
print(data)

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
