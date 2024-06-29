fp = open("python.txt", "r")
print(fp.readlines())

fp = open("python.txt", "a")
fp.write(" python is the best by python x")
fp.close()
