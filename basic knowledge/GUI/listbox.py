from tkinter import *

def callbutton1():
    for i in listb.curselection():     # 檢查選取項
        listb2.insert(0, listb.get(i)) # 新增至右側列表方塊

def callbutton2():
    for i in listb.curselection():
        listb2.delete(i)

root = Tk()
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
listb = Listbox(root)
listb2 = Listbox(root)
for item in li:
    listb.insert(0, item)              # 左側列表方塊元件插入資料
listb.grid(row=0, column=0, rowspan=2) # 將列表方塊元件放置到視窗物件中
b1 = Button(root, text="add>>", command=callbutton1, width=20)
b2 = Button(root, text="del<<", command=callbutton2, width=20)
b1.grid(row=0, column=1, rowspan=2)
b2.grid(row=1, column=1, rowspan=2)
listb2.grid(row=0, column=2, rowspan=2)
root.mainloop()