class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for i in range(3):
            print('|'.join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print('-----')

    def is_winner(self, player):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def is_draw(self):
        return ' ' not in self.board

    def minimax(self, depth, alpha, beta, is_maximizing):
        if self.is_winner('X'):
            return 1
        elif self.is_winner('O'):
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score = self.minimax(depth + 1, alpha, beta, False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score = self.minimax(depth + 1, alpha, beta, True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
            return best_score

    def best_move(self):
        best_score = float('-inf')
        move = -1
        alpha = float('-inf')
        beta = float('inf')
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                score = self.minimax(0, alpha, beta, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def player_move(self):
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if self.board[move] == ' ':
                    self.board[move] = 'O'
                    break
                else:
                    print("Invalid move! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    game = TicTacToe()
    while True:
        game.print_board()
        if game.is_draw():
            print("It's a draw!")
            break
        if game.is_winner('O'):
            print("O wins!")
            break

        game.player_move()

        if game.is_draw():
            game.print_board()
            print("It's a draw!")
            break

        if game.is_winner('O'):
            game.print_board()
            print("O wins!")
            break

        print("AI's turn (X):")
        move = game.best_move()
        if move != -1:
            game.board[move] = 'X'

        if game.is_winner('X'):
            game.print_board()
            print("X wins!")
            break
