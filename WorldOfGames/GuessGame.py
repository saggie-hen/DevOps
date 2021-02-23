from abc import ABC
import random


class GuessGame(ABC):

    def __init__(self, difficulty):
        self.secretNumber = self.generate_number(difficulty)
        self.difficulty = difficulty
        super().__init__()

    def get_secret_number(self):
        print(self.secretNumber)

    def get_guess_from_user(self):
        guess = int(input(f"Guess a number between 1 to {self.difficulty}")) # this is not safe, do input validation before casting to int
        return guess

    def compare_results(self):
        guess = self.get_guess_from_user()
        if guess == self.secretNumber:
            return True
        return False

    def play(self):
        result = self.compare_results()
        if result:
            print("You Won!")
        else:
            print("You Lose!")
            print(f"The number is {self.secretNumber}")

    @staticmethod
    def generate_number(difficulty):
        return random.randint(1, difficulty)
