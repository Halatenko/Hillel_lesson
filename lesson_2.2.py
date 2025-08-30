a = int(input("Enter a five-digit number: "))

b = (a // 10000)
c = ((a // 1000) % 10)
d = ((a // 100) % 10)
e = ((a // 10) % 10)
f = (a % 10)

print(f, e, d, c, b)