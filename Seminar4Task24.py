arr = [5, 8, 6, 4, 9, 2, 7, 3]
max_b = 0
# for i in range(0, len(arr)):
#     temp_m = sum(arr[i-1:i+2])
#     max_b = temp_m if temp_m > max_b else max_b

print(max(list(sum([arr[i-1], arr[i], arr[(i+1) % len(arr)]]) for i in range(0, len(arr)))))

