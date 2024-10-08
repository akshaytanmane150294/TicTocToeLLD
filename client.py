from controllers.controllers import *
from models.models import Player, Bot, Symbol
from models.enums import GameStatus, PlayerType, DifficultyLevel
from Stratagies.WinningStrategy import RowWinningStrategy, ColumnWinningStrategy, DiagonalWinningStrategy


def main():
    GC = GameController()
    dim = 3
    players = [
        Player(name="Pratyay", symbol=Symbol(
            "X"), playerType=PlayerType.HUMAN),
        Bot(name='Alien', symbol=Symbol('O'),
            difficultyLevel=DifficultyLevel.EASY)
    ]

    ws = [
        RowWinningStrategy(dim, players),
        ColumnWinningStrategy(dim, players),
        DiagonalWinningStrategy(players)
    ]
    game = GC.createGame(dimension=dim, players=players, winningstrategies=ws)
    print("Game is Staring")
    while (GC.getGameStatus(game) == GameStatus.INPROGESS):
        print("-----------Board---------")
        GC.displayboard(game)

        undo = input('Does anyone want to UNDO? Y/N \n ')
        if (undo == "Y"):
            GC.UNDO(game)
            continue
        else:
            GC.makeMove(game)
        GC.displayboard(game)
        GC.displayboard(game)


main()
