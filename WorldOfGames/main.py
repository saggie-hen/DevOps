from Live import welcome, load_game
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame

welcome("Saggie")
gameNumber, gameDifficulty = load_game()

if gameNumber == 1:
    game = MemoryGame(gameDifficulty)
    game.play()
elif gameNumber == 2:
    game = GuessGame(gameDifficulty)
    game.play()
elif gameNumber == 3:
    game = CurrencyRouletteGame(gameDifficulty)
    game.play()
