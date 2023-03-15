# *** (1)У вас есть массив чисел, составьте из них максимальное число. Например:

#                                  [61, 228, 9] -> 961228


array = [61, 228, 9]

str_n1 = int(f"{array[0]}{array[1]}{array[2]}")
str_n2 = int(f"{array[0]}{array[2]}{array[1]}")
str_n3 = int(f"{array[1]}{array[0]}{array[2]}")
str_n4 = int(f"{array[1]}{array[2]}{array[0]}")
str_n5 = int(f"{array[2]}{array[0]}{array[1]}")
str_n6 = int(f"{array[2]}{array[1]}{array[0]}")

arr = [str_n1, str_n2, str_n3, str_n4, str_n5, str_n6]
max_number = 0
i = 0
for i in arr:
    if i >= max_number:
        max_number = i

print(f"Максимальное число: {max_number}")







# max_number = 0
# i = 0
# while i in arr:
#     if arr[i] >= max_number:
#         max_number = arr[i]

# print(f"Максимальное число: {max_number}")



