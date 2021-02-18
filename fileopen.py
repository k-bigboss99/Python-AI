file = open("./hello.txt")
context1 = file.read()
file.close()
print(context1)

file = open("./hello.txt")
context2 = ""
while True:
    fragment = file.read(5) # 設定參數一次讀取3字元
    if fragment == "":
        break
    context2 += fragment
    print(" ")
file.close()
print(context2)

file = open("./hello.txt")
context3 = ""
while True:
    line = file.readline() 
    if line == "":
        break
    context3 += line
    print(" ")
file.close()
print(context3)

file = open("./hello.txt")
context4 = file.readlines()
file.close()
print(context4)
for line in context4:
    print(line)

