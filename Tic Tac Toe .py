import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [""] * 9
game_over = False

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="TIC-TAC-TOE",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

status = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 18)
)
status.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []


def check_winner():
    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def click_button(index):
    global current_player, game_over

    if board[index] != "" or game_over:
        return

    board[index] = current_player
    buttons[index].config(
        text=current_player,
        state="disabled"
    )

    result = check_winner()

    if result:
        game_over = True

        if result == "Draw":
            status.config(text="It's a Draw!")
            messagebox.showinfo("Game Over", "It's a Draw!")
        else:
            status.config(text=f"Player {result} Wins!")
            messagebox.showinfo(
                "Game Over",
                f"Player {result} Wins!"
            )

        return

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    status.config(text=f"Player {current_player}'s Turn")


def restart_game():
    global current_player, board, game_over

    current_player = "X"
    board = [""] * 9
    game_over = False

    status.config(text="Player X's Turn")

    for button in buttons:
        button.config(
            text="",
            state="normal"
        )


for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Arial", 30, "bold"),
        width=5,
        height=2,
        command=lambda i=i: click_button(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    buttons.append(button)


restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 15, "bold"),
    command=restart_game
)

restart_button.pack(pady=20)

root.mainloop()