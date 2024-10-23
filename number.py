import tkinter as tk
import random

class NumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Game")
        self.buttons = []
        self.create_buttons()
        self.reset_game()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.master, text="", width=5, height=2,
                               command=lambda index=i: self.player_move(index))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def reset_game(self):
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL)
        self.current_player = 'X'

    def player_move(self, index):
        if self.buttons[index]["text"] == "":
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
                self.disable_buttons()
            else:
                self.current_player = 'O'
                self.ai_move()

    def ai_move(self):
        available_moves = [i for i in range(9) if self.buttons[i]["text"] == ""]
        if available_moves:
            move = random.choice(available_moves)
            self.buttons[move].config(text=self.current_player)
            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
                self.disable_buttons()
            else:
                self.current_player = 'X'

    def check_winner(self, player):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        return any(all(self.buttons[i]["text"] == player for i in condition) for condition in win_conditions)

    def show_winner(self, player):
        winner_window = tk.Toplevel(self.master)
        winner_window.title("Game Over")
        label = tk.Label(winner_window, text=f"{player} wins!")
        label.pack(padx=20, pady=20)
        ok_button = tk.Button(winner_window, text="OK", command=winner_window.destroy)
        ok_button.pack(pady=(0, 20))

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGame(root)
    root.mainloop()
