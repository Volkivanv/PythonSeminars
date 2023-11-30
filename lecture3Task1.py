
#import module1
#from module1 import max1
#from module1 import *
import module1 as m1


def sum_number(n, y='Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res


print(sum_number(5, 'adfa'))

print(sum_str('f', 'g', 'k', 'h'))

# can only concatenate str (not "int") to str
#print(sum_str(1, 8, 8))

print(m1.max1(5, 9))
