def copy_file(oldfile, newfile):
    oldfile = open(oldfile, "r")
    newfile = open(newfile, "w")
    while True:
        context = oldfile.read(50)
        if context == "":
            break
        newfile.write(context)
    oldfile.close()
    newfile.close()
    return

copy_file("./hello.txt", "./test.txt")