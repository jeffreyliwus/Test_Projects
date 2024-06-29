name = "Python X"

try:
    print(name)
except NameError:
    print("some error occured")


try:
    print(name)
except NameError as e:
    print("Some error occurred. Please contact Developer: ", e)

# number1 = int(input("enter first number: "))
# number2 = int(input("enter second number: "))

# print("Division is:", number1 / number2)

try:
    number1 = int(input("enter first number: "))
    number2 = int(input("enter second number: "))

    print("Division is:", number1 / number2)

except Exception as e:
    print("cannot divide by zero")

finally:
    print("Thank you for using our calculator")
