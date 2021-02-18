file = open("./test.txt", "w")
file.write("first line.\nsecond line\n")
file.close()

file = open("./test.txt", "a")
file.write("third line.")
file.close()

file = open("./test.txt")
context = file.read()
file.close()
print(context)