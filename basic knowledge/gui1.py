import tkinter
win = tkinter.Tk()                              # 建立Windows視窗物件
win.title("HelloWorld")                         # 設定視窗標題
win.geometry("200x200")                
label = tkinter.Label(win, text="hello, python")
label.pack()                                    # 將Label元件增加到視窗中顯示
button1 = tkinter.Button(win, text="BUTTON1")
button1.pack(side = tkinter.LEFT)               # 將button1元件增加到視窗中顯示，左停駐
button2 = tkinter.Button(win, text="BUTTON2")
button2.pack(side = tkinter.RIGHT)              # 將button1元件增加到視窗中顯示，右停駐
win.mainloop()           # 進入訊息循環，顯示視窗
