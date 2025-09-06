list = [11, 3, 0, 5, 0, 4]

a = 0
b = 0
while a < len(list):
    if list[a] != 0:
        list[b] = list[a]
        if a != b:
            list[a] = 0
        b += 1
    a += 1
print(list)