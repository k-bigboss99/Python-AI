import tkinter as tk
import random
number = random.randint(0, 1024)
running = True
count = 0                       # 猜的次數
number_max = 1024
number_min = 0

def eBtnClose(event):
    root.destory()

def eBtnGuess(event):
    global number_max
    global number_min
    global count
    global running
    if running:
        guess = int(entry_a.get())
        if guess == number:
            labelqval("Congratulations")
            count = count + 1
            running = False
            numGuess()
        elif guess < number:
            if guess > number_min:
                number_min = guess  # 修改範圍最小數
                count = count + 1
                labelqval("too small, please input" + str(number_min) + "to" + str(number_max) + "'s number")
        else:
            if guess < number_max:
                number_max = guess
                count = count + 1
                labelqval("too small, please input" + str(number_min) + "to" + str(number_max) + "'s number")
    else:
        labelqval("It's finished")

def numGuess():
    labelqval("try times: " + str(count))

def labelqval(vText):
    label_val_q.config(label_val_q, text=vText)

root = tk.Tk()
root.geometry("400x90+200+200")
label_val_q = tk.Label(root, width="80")
label_val_q.pack(side="top")

entry_a = tk.Entry(root, width="40")
btnGuess = tk.Button(root, text="guess")
entry_a.pack(side="left")
entry_a.bind('<Return>', eBtnGuess)      # 綁定事件
btnGuess.bind('<Button-1>', eBtnGuess)
btnGuess.pack(side="left")

btnClose = tk.Button(root, text="close")
btnClose.bind('<Button-1>', eBtnClose)
btnClose.pack(side="left")
labelqval("please input a number between 0-1024: ")
entry_a.focus_set()
print(number)
root.mainloop()

