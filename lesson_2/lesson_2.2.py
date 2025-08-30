a = int(input("Enter a five-digit number: "))

b = (a // 10000)
c = ((a // 1000) % 10)
d = ((a // 100) % 10)
e = ((a // 10) % 10)
f = (a % 10)

reverse_a = f*10000 + e*1000 + d*100 + c*10 + b
print(reverse_a)