list = [11, 23, 34, 45, 56, 67, 78, 89, 90]


middle_list = (len(list) + 1) // 2
a = list[:middle_list]
b = list[middle_list:]
print([a, b])