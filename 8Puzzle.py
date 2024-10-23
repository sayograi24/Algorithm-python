import tkinter as tk
import random

class PuzzleGame:
    def __init__(self, master):
        self.master = master
        self.master.title("8 Puzzle Game")
        self.tiles = list(range(1, 9)) + [0]  # 0 represents the blank tile
        self.blank_index = 8
        self.create_widgets()
        self.update_tiles()

    def create_widgets(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text="", width=5, height=2,
                               command=lambda index=i: self.on_tile_click(index))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.shuffle_button = tk.Button(self.master, text="Shuffle", command=self.shuffle_tiles)
        self.shuffle_button.grid(row=3, column=0, columnspan=3)

    def update_tiles(self):
        for i, button in enumerate(self.buttons):
            if self.tiles[i] == 0:
                button.config(text="", bg="white")
            else:
                button.config(text=str(self.tiles[i]), bg="lightblue")

    def on_tile_click(self, index):
        if self.can_move(index):
            self.swap_tiles(index)
            self.update_tiles()

    def can_move(self, index):
        row, col = index // 3, index % 3
        blank_row, blank_col = self.blank_index // 3, self.blank_index % 3

        return (abs(row - blank_row) + abs(col - blank_col) == 1)

    def swap_tiles(self, index):
        self.tiles[self.blank_index], self.tiles[index] = self.tiles[index], self.tiles[self.blank_index]
        self.blank_index = index

    def shuffle_tiles(self):
        random.shuffle(self.tiles)
        self.blank_index = self.tiles.index(0)
        self.update_tiles()

if __name__ == "__main__":
    root = tk.Tk()
    game = PuzzleGame(root)
    root.mainloop()
