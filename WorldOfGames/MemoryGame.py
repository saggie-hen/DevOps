from abc import ABC
import random
import time
import sys


class MemoryGame(ABC):

    def __init__(self, difficulty):
        self.difficulty = difficulty
        super().__init__()

    def play(self):
        randomlist = self.generate_list(self.difficulty)
        userlist   = self.get_list_from_user(self.difficulty)
        result     = self.compare_results(randomlist, userlist)
        if(result):
            print("You Won!")
        else:
            print("You Lose!")

    @staticmethod
    def compare_results(randomlist, userlist):
        if(randomlist == userlist):
            return True
        return False

    @staticmethod
    def generate_list(difficulty):
        random_list = []
        for i in range(difficulty):
            num = random.randint(1, 101)
            random_list.append(num)
        sys.stdout.write(" ".join(str(x) for x in random_list))
        time.sleep(0.7)
        sys.stdout.write('\r')
        sys.stdout.flush()
        return random_list

    @staticmethod
    def get_list_from_user(difficulty):
        user_list = []
        for i in range(difficulty):
            num = int(input("enter number between 1 to 101"))
            user_list.append(num)
        return user_list
