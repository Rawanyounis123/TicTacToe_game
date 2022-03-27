from tkinter import *
from tkinter import ttk
from tkinter import messagebox

active_player = 1
p1 = []
p2 = []

row1 = []
row2 = []
row3 = []

col1 = []
col2 = []
col3 = []

moves_1 = [1, 3, 5, 7, 9]
moves_2 = [0, 2, 4, 6, 8]

root = Tk()
root.title("Tic Tac Toe : player 1")
style = ttk.Style()
style.theme_use('xpnative')

bu1 = ttk.Button(root, text=" ")
bu1.grid(row=0, column=0, sticky="s n e w", ipadx=40, ipady=40)
entry1 = Entry(root)
entry1.grid(row=1, column=0, sticky="s n e w", ipadx=10, ipady=10)
bu1.config(command=lambda: buclick(1))

bu2 = ttk.Button(root, text=" ")
bu2.grid(row=0, column=1, sticky="s n e w", ipadx=40, ipady=40)
entry2 = Entry(root)
entry2.grid(row=1, column=1, sticky="s n e w", ipadx=10, ipady=10)
bu2.config(command=lambda: buclick(2))

bu3 = ttk.Button(root, text=" ")
bu3.grid(row=0, column=2, sticky="s n e w", ipadx=40, ipady=40)
entry3 = Entry(root)
entry3.grid(row=1, column=2, sticky="s n e w", ipadx=10, ipady=10)
bu3.config(command=lambda: buclick(3))

bu4 = ttk.Button(root, text=" ")
bu4.grid(row=2, column=0, sticky="s n e w", ipadx=40, ipady=40)
entry4 = Entry(root)
entry4.grid(row=3, column=0, sticky="s n e w", ipadx=10, ipady=10)
bu4.config(command=lambda: buclick(4))

bu5 = ttk.Button(root, text=" ")
bu5.grid(row=2, column=1, sticky="s n e w", ipadx=40, ipady=40)
entry5 = Entry(root)
entry5.grid(row=3, column=1, sticky="s n e w", ipadx=10, ipady=10)
bu5.config(command=lambda: buclick(5))

bu6 = ttk.Button(root, text=" ")
bu6.grid(row=2, column=2, sticky="s n e w", ipadx=40, ipady=40)
entry6 = Entry(root)
entry6.grid(row=3, column=2, sticky="s n e w", ipadx=10, ipady=10)
bu6.config(command=lambda: buclick(6))

bu7 = ttk.Button(root, text=" ")
bu7.grid(row=4, column=0, sticky="s n e w", ipadx=40, ipady=40)
entry7 = Entry(root)
entry7.grid(row=5, column=0, sticky="s n e w", ipadx=10, ipady=10)
bu7.config(command=lambda: buclick(7))

bu8 = ttk.Button(root, text=" ")
bu8.grid(row=4, column=1, sticky="snew", ipadx=40, ipady=40)
entry8 = Entry(root)
entry8.grid(row=5, column=1, sticky="s n e w", ipadx=10, ipady=10)
bu8.config(command=lambda: buclick(8))

bu9 = ttk.Button(root, text=" ")
bu9.grid(row=4, column=2, sticky="snew", ipadx=40, ipady=40)
entry9 = Entry(root)
entry9.grid(row=5, column=2, sticky="s n e w", ipadx=10, ipady=10)
bu9.config(command=lambda: buclick(9))


def buclick(id):
    global active_player
    global p1
    global p2
    if active_player == 1:
        if setlayout(id):
            checkWinner()
            root.title("Tic Tac Toe : player 2")
            active_player = 2
        else:
            root.title("Tic Tac Toe : player 1")
            active_player = 1
    elif active_player == 2:
        if setlayout(id):
            checkWinner()
            root.title("Tic Tac Toe : player 1")
            active_player = 1
        else:
            root.title("Tic Tac Toe : player 2")
            active_player = 2


def isvalid(num, player, id):
    n = int(num[0])
    if player == 1:
        if n not in moves_1:
            messagebox.showinfo(title="Try Again", message="Invalid input ,remaining moves are {}".format(moves_1))
            return 0
        else:
            p1.append(id)
            moves_1.remove(n)
            return 1
    elif player == 2:
        if n not in moves_2:
            messagebox.showinfo(title="Try Again", message="Invalid input,remaining1 moves are {}".format(moves_2))
            return 0
        else:
            p2.append(id)
            moves_2.remove(n)
            return 1


def setlayout(id):
    if id == 1:
        if not isvalid(entry1.get(), active_player, id):
            entry1.delete(0, END)
            return 0
        else:
            bu1.config(text=entry1.get())
            bu1.state(['disabled'])
            entry1.config(state="disabled")
            row1.append(entry1.get())
            col1.append(entry1.get())
            return 1
    elif id == 2:
        if not isvalid(entry2.get(), active_player, id):
            entry2.delete(0, END)
            return 0
        else:
            bu2.config(text=entry2.get())
            bu2.state(['disabled'])
            entry2.config(state="disabled")
            row1.append(entry2.get())
            col2.append(entry2.get())
            return 1
    elif id == 3:
        if not isvalid(entry3.get(), active_player, id):
            entry2.delete(0, END)
            return 0
        else:
            bu3.config(text=entry3.get())
            bu3.state(['disabled'])
            entry3.config(state="disabled")
            row1.append(entry3.get())
            col3.append(entry3.get())
            return 1
    elif id == 4:
        if not isvalid(entry4.get(), active_player, id):
            entry4.delete(0, END)
            return 0
        else:
            bu4.config(text=entry4.get())
            bu4.state(['disabled'])
            row2.append(entry4.get())
            col1.append(entry4.get())
            entry4.config(state="disabled")
            return 1
    elif id == 5:
        if not isvalid(entry5.get(), active_player, id):
            entry5.delete(0, END)
            return 0
        else:
            bu5.config(text=entry5.get())
            bu5.state(['disabled'])
            row2.append(entry5.get())
            col2.append(entry5.get())
            entry5.config(state="disabled")
            return 1
    elif id == 6:
        if not isvalid(entry6.get(), active_player, id):
            entry6.delete(0, END)
            return 0
        else:
            bu6.config(text=entry6.get())
            bu6.state(['disabled'])
            row2.append(entry6.get())
            col3.append(entry6.get())
            entry6.config(state="disabled")
            return 1
    elif id == 7:
        if not isvalid(entry7.get(), active_player, id):
            entry7.delete(0, END)
            return 0
        else:
            bu7.config(text=entry7.get())
            bu7.state(['disabled'])
            row3.append(entry7.get())
            col1.append(entry7.get())
            entry7.config(state="disabled")
            return 1
    elif id == 8:
        if not isvalid(entry8.get(), active_player, id):
            entry8.delete(0, END)
            return 0
        else:
            bu8.config(text=entry8.get())
            bu8.state(['disabled'])
            row3.append(entry8.get())
            col2.append(entry8.get())
            entry8.config(state="disabled")
            return 1
    elif id == 9:
        if not isvalid(entry9.get(), active_player, id):
            entry9.delete(0, END)
            return 0
        else:
            bu9.config(text=entry9.get())
            bu9.state(['disabled'])
            row3.append(entry9.get())
            col3.append(entry9.get())
            entry9.config(state="disabled")
            return 1


def checkWinner():
    winner = -1
    total1 = 0

    for num in row1:
        total1 += int(num)
    if total1 == 15 and len(row1) == 3:
        winner = active_player

    total2 = 0
    for num in row2:
        total2 += int(num)
    if total2 == 15 and len(row2) == 3:
        winner = active_player

    total3 = 0
    for num in row3:
        total3 += int(num)
    if total3 == 15 and len(row3) == 3:
        winner = active_player

    totalc1 = 0
    for num in col1:
        totalc1 += int(num)
    if totalc1 == 15 and len(col1) == 3:
        winner = active_player

    totalc2 = 0
    for num in col2:
        totalc2 += int(num)
    if totalc2 == 15 and len(col2) == 3:
        winner = active_player

    totalc3 = 0
    for num in col3:
        totalc3 += int(num)
    if totalc3 == 15 and len(col3) == 3:
        winner = active_player

    if winner == 1:
        messagebox.showinfo(title="Congrats", message="Player 1 is the winner!")
    if winner == 2:
        messagebox.showinfo(title="Congrats", message="Player 2 is the winner!")
    if len(p1) + len(p2) == 9 and not (winner == 1) and not (winner == 2):
        messagebox.showinfo(title="Try Again", message="Draw!")


root.mainloop()
