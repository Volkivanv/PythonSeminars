list_1 = [6, 1, 2, 3, 4, 5, 8, 7]
k = 6
answer = list_1[0]
for item in list_1:
    if abs(item - k) < abs(answer - k):
        answer = item

print(answer)
