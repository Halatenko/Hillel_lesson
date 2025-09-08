list = [2, 3, 9, 7, 6, 4, 5]

a = 0
b = 0
while a < len(list):
    if a % 2 == 0:
        b += list[a]
    a += 1
print(b * list[-1])