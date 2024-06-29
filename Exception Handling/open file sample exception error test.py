try:
    fp = open("python1.txt", "r")
    print(fp.readlines())

    fp = open("python.txt", "a")
    fp.write(" python is the best by python x")
    fp.close()

except FileNotFoundError:
    print("file not found")
