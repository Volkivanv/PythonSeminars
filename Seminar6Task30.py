# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 ,
# разность d и количество элементов n будет задано автоматически. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.


a1 = 2
d = 3
n = 4

print("\n".join(list(str(i) for i in range(a1, a1 + n * d, d))))
