class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # 3x3 board
        self.current_player = "X"

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def is_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]               # diagonal
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False

    def is_draw(self):
        return " " not in self.board

    def play(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            self.print_board()
            move = input(f"Player {self.current_player}, enter your move (1-9): ")

            try:
                move = int(move) - 1
                if self.board[move] == " ":
                    self.board[move] = self.current_player
                    if self.is_winner():
                        self.print_board()
                        print(f"Player {self.current_player} wins!")
                        break
                    if self.is_draw():
                        self.print_board()
                        print("It's a draw!")
                        break
                    self.current_player = "O" if self.current_player == "X" else "X"
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
