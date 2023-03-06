import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("290x310")

# create rain image
default_rain = Image.open("rain.png")
resize_rain = default_rain.resize((50, 50))
rain = ImageTk.PhotoImage(resize_rain)

# create penguin image
default_pen = Image.open("penguin.png")
resize_pen = default_pen.resize((50, 50))
pen = ImageTk.PhotoImage(resize_pen)

default_board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

def win():
    if count_2 % 2 == 0:
        tk.Label(root, text="Rain wins!").grid(row=2, column=1)
    else:
        tk.Label(root, text="Penguin wins!").grid(row=2, column=1)

def check():
    x = 0
    for sublist in default_board:
        if len(sublist) == 3 and len(set(sublist)) == 1:
            win()
    if default_board[0][0] == default_board[1][1] == default_board[2][2]: # diagonal
        if default_board[0][0] and default_board[1][1] and default_board[2][2] != "_":
            win()
    elif default_board[0][2] == default_board[1][1] == default_board[2][0]: # diagonal
        if default_board[0][2] and default_board[1][1] and default_board[2][0] != "_":
            win()
    elif default_board[0][0] == default_board[1][0] == default_board[2][0]: # column 1
        if default_board[0][0] and default_board[1][0] and default_board[2][0] != "_":
            win()
    elif default_board[0][1] == default_board[1][1] == default_board[2][1]: # column 2
        if default_board[0][1] and default_board[1][1] and default_board[2][1] != "_":
            win()
    elif default_board[0][2] == default_board[1][2] == default_board[2][2]: # column 3
        if default_board[0][2] and default_board[1][2] and default_board[2][2] != "_":
            win()

# image onto button
count_2 = 0
def tic(row, column):
    global count_2
    count_2 += 1 # keep track of which is "O" and "X"
    if count_2 % 2 == 0:
        tk.Button(root, image=rain, width=6, height=5).grid(row=row, column=column, sticky="nesw")
        default_board[row-1].insert(column, "X")
        default_board[row-1].pop(column+1)
    else:
        tk.Button(root, image=pen, width=6, height=5).grid(row=row, column=column, sticky="nesw")
        default_board[row-1].insert(column, "O")
        default_board[row - 1].pop(column + 1)
    print(default_board)
    if count_2 >= 5:
        check()
    if count_2 == 9:
        tk.Label(root, text="Tie!").grid(row=2, column=1)

# create tic-tac-toe board
row = 0
column = 0
count = 0
for i in range(1, 10):
    if count % 3 == 0:
        row += 1
        column = 0
    tk.Button(root, width=6, height=5, command=lambda row=row, column=column: tic(row, column)).grid(row=row, column=column, sticky="nesw")
    column += 1
    count += 1

root.mainloop()