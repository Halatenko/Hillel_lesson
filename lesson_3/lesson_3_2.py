list3 = [1, 'F', 2, 3, 4, 5]
if list3 == []:
    print(list3)
else:
    move_element = list3.pop()
    list3.insert(0, move_element)
    print(list3)