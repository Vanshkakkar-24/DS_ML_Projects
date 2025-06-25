# Simple Calculator

while True:
    num1 = int(input("Enter first number: "))
    oper = input("Enter operator: ")
    num2 = int(input("Enter second number: "))
    if oper == '+':
        res = num1 + num2
        print("Addition of ", num1, " and ", num2, " is: ", res)
    elif oper == '-':
        res = num1 - num2
        print("Subtraction of ", num1, " and ", num2, " is: ", res)
    elif oper == '*':
        res = num1 * num2
        print("Multiplication of ", num1, " and ", num2, " is: ", res)
    elif oper == '/':
        if num2 != 0:
            res = num1 / num2
            print("Division of ", num1, " and ", num2, " is: ", res)
        else:
            print("Cannot divide the numerator with 0")
    else:
        print("Enter a valid operator")