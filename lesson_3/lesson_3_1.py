num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
math_oper = input("Enter a math operation: ")

if math_oper == "+":
    a = num1 + num2
    print("Answer: ", a)
elif math_oper == "-":
    b = num1 - num2
    print("Answer: ", b)
elif math_oper == "*":
    c = num1 * num2
    print("Answer: ", c)
elif math_oper == "/":
    if num2 >= 1:
        d = num1 / num2
        print("Answer: ", d)
    elif num2 == 0:
        print("You cannot divide by zero!")
else:
    print("Incorrect operation!")