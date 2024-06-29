import Calculator

a = int(input("enter 1st number: "))
b = int(input("enter 2st number: "))
arit = input("choose your aritmethic operation: ")

if arit == "+":
    total = Calculator.add(a, b)
    print("your ans is: ", total)
elif arit == "-":
    total = Calculator.subtract(a, b)
    print("your ans is: ", total)
elif arit == "/":
    total = Calculator.divide(a, b)
    print("your ans is: ", total)
elif arit == "*":
    total = Calculator.multiply(a, b)
    print("your ans is: ", total)
else:
    print("wrong arithimetic operation ")
