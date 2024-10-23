import random

class NumberGuessingGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.guesses_taken = 0

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        
        while True:
            guess = input("Take a guess: ")

            try:
                guess = int(guess)
                self.guesses_taken += 1

                if guess < self.target_number:
                    print("Your guess is too low.")
                elif guess > self.target_number:
                    print("Your guess is too high.")
                else:
                    print(f"Congratulations! You've guessed the number {self.target_number} in {self.guesses_taken} guesses!")
                    break
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()
