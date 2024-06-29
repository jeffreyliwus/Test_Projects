try:
    a = int(input("enter a positive integer: "))
    if a <= 0:
        raise ValueError("its not a positive integer")
except ValueError as e:
    print(e)
