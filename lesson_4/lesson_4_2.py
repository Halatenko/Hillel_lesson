list = [2, 3, 9, 7, 6, 4, 5]

if list == []:
    print([])
else:
    a = len(list)
    b = 0
    c = 0
    while b < a:
        if b % 2 == 0:
            c += list[b]
        b += 1
    print(c * list[-1])