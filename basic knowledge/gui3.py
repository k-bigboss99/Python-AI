from tkinter import *
root = Tk()                                  
root.title("Login")                          
root['width'] = 300; root['height'] = 100
Label(root, text="username", width=6).place(x=50, y=2) # 絕對座標(50,2)
Entry(root, width=20).place(x=100,y=2)
Label(root, text="password", width=6).place(x=50, y=20)
Entry(root, width=20, show='*').place(x=100,y=20)
Button(root, text="login", width=8).place(x=100,y=40)
Button(root, text="cancel", width=8).place(x=200,y=40)
root.mainloop()


