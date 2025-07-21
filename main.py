import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("270x350")

current_player = "X"
buttons = []

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

    if buttons[row][col]['text'] != "":
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")

    if check_draw():
        messagebox.showinfo("Игра окончена", f"Боевая ничья!")

    current_player = "0" if current_player == "X" else "X"

def reset_game():
    global current_player

    for i in range(3):
        buttons[i][0]["text"] = ""
        buttons[i][1]["text"] = ""
        buttons[i][2]["text"] = ""
        current_player = "X"

def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False
    return True

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

# Add reset game button
button1 = tk.Button(window, text="Reset Game", width=11, command = reset_game)
button1.grid(row=3, column=1)

button2 = tk.Button(window, text="Game Begin 0", width=11, command = game_begin_0)
button2.grid(row=4, column=1)



window.mainloop()

