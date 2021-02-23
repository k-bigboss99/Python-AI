import sqlite3

def opendb():
    conn = sqlite3.connect("./student.db")
    cur = conn.execute("create table if not exists tongxinlu(usernum integer primary key, username varchar(128), password varchar(128), address varchar(125), telnum varchar(128))")
    return cur, conn

def showalldb():
    print("====================process====================")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("select * from tongxinlu")
    res = cur.fetchall()
    for line in res:
        for h in line:
            print(h)
    cur.close()

def into():
    usernum = input("enter ID: ")
    username = input("enter name: ")
    password = input("enter password: ")
    address = input("enter address: ")
    telnum = input("enter telnumber: ")
    return usernum, username, password, address, telnum

def adddb():
    print("""--------------------add--------------------""")
    person = into()
    hel = opendb()
    hel[1].execute("insert into tongxinlu(usernum, username, password, address, telnum)values(?,?,?,?,?)", (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    print("--------------------add success--------------------")
    showalldb()
    hel[1].close()

def deldb():
    print("""--------------------del--------------------""")
    delchoice = input("enter a ID: ")
    hel = opendb()
    hel[1].execute("delete from tongxinlu where usernum = " + delchoice)
    hel[1].commit()
    print("""--------------------del success--------------------""")
    showalldb()
    hel[1].close()

def alter():
    print("""--------------------alter--------------------""")
    changechoice = input("enter a ID: ")
    hel = opendb()
    person = into()
    hel[1].execute("update tongxinlu set usernum=?, username=?, password=?, address=?, telnum=? where usernum=" + changechoice, (person[0], person[1], person[2], person[3], person[4]))
    hel[1].commit()
    showalldb()
    hel[1].close()

def searchdb():
    print("""--------------------search--------------------""")
    choice = input("enter a ID: ")
    hel = opendb()
    cur = hel[1].cursor()
    cur.execute("select * from tongxinlu where usernum=" + choice)
    hel[1].commit()
    print("""--------------------search success--------------------""")
    for row in cur:
        print(row[0], row[1], row[2], row[3], row[4])
    cur.close()
    hel[1].close()

def conti(a):
    choice = input("continue? (Y/N): ")
    if choice == 'Y' or choice == 'y':
        a = 1
    else:
        a = 0
    return a

if __name__ == "__main__":
    flag = 1
    while(flag):
        print("""--------------------welcome to students' db--------------------""")
        choiceshow = """
        請選擇您的選項 : 
        (1)新增資料庫內容
        (2)刪除資料庫內容
        (3)修改資料庫內容
        (4)查詢資料庫內容
        """
        choice = int(input(choiceshow))
        if choice == 1:
            adddb()
            conti(flag)
        elif choice == 2:
            deldb()
            conti(flag)
        elif choice == 3:
            alter()
            conti(flag)
        elif choice == 4:
            searchdb()
            conti(flag)
        else:
            print("error please input again")