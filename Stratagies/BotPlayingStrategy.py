from abc import abstractmethod
from models.enums import *

"""
The BotplayingStrategy class is an abstract class, 
which means it is meant to be a blueprint for other classes. 
You cannot create an instance of this class directly.

    """


class BotplayingStrategy:

    @abstractmethod
    def makeMove(self, board):
        pass


class EASYBotPlayingStrategy(BotplayingStrategy):
    def makeMove(self, board):
        for i in range(board.size):
            for j in range(board.size):
                if (board.grid[i][j].state == CellState.EMPTY):
                    return board.grid[i][j]
        return None


class MEDIUMBotPlayingStrategy(BotplayingStrategy):
    def makeMove(self, board):
        return None


class HARDBotPlayingStrategy(BotplayingStrategy):
    def makeMove(self, board):
        return None


class BotPlaynigStrategyFactory:
    """For simplifying we will return one Strategy"""
    def getBotPlayingStrategyforDifficultyLevel(dl):
        return EASYBotPlayingStrategy()
        # if (dl == DifficultyLevel.EASY):
        #     return EASYBotPlayingStrategy()
        # elif (dl == DifficultyLevel.MEDIUM):
        #     return MEDIUMBotPlayingStrategy()
        # else:
        #     return HARDBotPlayingStrategy()
