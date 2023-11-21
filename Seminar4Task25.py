# s = 'a a a b c a a d c d d'
# s = s.split()
# print(s)
# out_s = []
# dict1 = {}
# for i in s:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
#     out_s.append(i + '_' + str(dict1[i]))
# out_s = ' '.join(out_s)
# print(out_s)



# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

lst = "a a a b c a a d c d d".split()
print(lst)
dct = {}
for item in lst:
    if item in dct:
        print(f"{item}_{dct[item]}", end=' ')
    else:
        print(item, end=' ')
    dct[item] = dct.get(item, 0) + 1

print(dct)
