def calc2(a):
    return a * a


def math(op, x, y):
    print(op(x, y))


# math(lambda a, b: a + b, 6, 5)
#
# lst = "1 2 3 4 5 6 7 8".split()
#
# lst2 = list(int(x)**2 for x in lst if int(x) % 2 == 0)
# print(lst2)

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 4, 5, 8, 23, 38]

res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x**2), res)

print(res)

data = [1, 2, 3, 4, 5, 8, 23, 38]

res = filter(lambda x: x % 2 == 0, data)
res = list(map(lambda x: (x, x*x), res))
print(res)


lst1 = ['кошка', 'курица', 'осел']
lst2 = [1, 2, 3]
lst3 = ['A', 'B', 'C']
print(list(zip(lst1, lst2, lst3)))
