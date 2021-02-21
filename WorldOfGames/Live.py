def welcome(name="Master"):
    print(f"Hello {name} and welcome to the World of Games(WoG).")
    print("Here you can find many cool games to play.")


def load_game():
    gameNumber = gameDifficulty = 0

    print("Please choose a game to play:")
    print("  1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("  2. Guess Game - guess a number and see if you chose like the computer")
    print("  3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    while not (gameNumber >= 1) or not (gameNumber <= 3):
        gameNumber = int(input("Please choose game from 1 to 3"))

    while not (gameDifficulty >= 1) or not (gameDifficulty <= 5):
        gameDifficulty = int(input("Please choose game difficulty from 1 to 5"))

    return gameNumber, gameDifficulty
