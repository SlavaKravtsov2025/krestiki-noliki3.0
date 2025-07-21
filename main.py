import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")

# set background color
window.configure(background="HotPink")

window.geometry("270x350")

current_player = "X"
buttons = []

# counts of winners
win_count_X = 0
win_count_0 = 0

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


def on_click(row, col):
    global current_player
    # declare using global variables
    global win_count_X
    global win_count_0

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        # increment of counts winner
        if current_player == "X":
            win_count_X += 1
            # show X winner count
            label1.configure(text = f"X winner - {win_count_X}")
        else:
            win_count_0 += 1
            # show 0 winner count
            label2.configure(text = f"0 winner - {win_count_0}")


    if check_draw():
        messagebox.showinfo("Игра окончена", f"Боевая ничья!")

    current_player = "0" if current_player == "X" else "X"

# begin new game with X
def reset_game():
    global current_player

    for i in range(3):
        buttons[i][0]["text"] = ""
        buttons[i][1]["text"] = ""
        buttons[i][2]["text"] = ""
        current_player = "X"

# check draw game
def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False
    return True

# begin new game with 0
def game_begin_0():
    global current_player
    reset_game()
    current_player = "0"

for i in range(3):
   row = []
   for j in range(3):
       btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
       btn.grid(row=i, column=j)
       row.append(btn)
   buttons.append(row)

# Add reset game button with X begin
button1 = tk.Button(window, text="Reset Game", width=11, command = reset_game)
button1.grid(row=3, column=1)

# add reset game button with 0 begin
button2 = tk.Button(window, text="Game Begin 0", width=11, command = game_begin_0)
button2.grid(row=4, column=1)

# X winner count
label1 = tk.Label(window, text="X winner - 0", width=11, bg="HotPink")
label1.configure(foreground="white")
label1.grid(row=3, column=0)

# 0 winner count
label2 = tk.Label(window, text="0 winner - 0", width=11, bg="HotPink")
label2.configure(foreground="white")
label2.grid(row=3, column=2)

window.mainloop()

