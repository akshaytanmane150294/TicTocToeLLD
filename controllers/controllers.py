from models.models import GameBuilder

""" INTERMEDIATE ABSTRCTION LAYER
    Why? Tomorrow the implementation details may change.
    we may have to change classes, create more subclasses.
    So use a loosely coupled object like Controller that talks.

"""


class GameController:
    def createGame(self, dimension, players, winningstrategies):
        return GameBuilder().setDimension(dimension).setPlayers(players).setwinningStrategies(winningstrategies).build()

    def displayboard(self, game):
        game.printBoard()

    def UNDO(self, game):
        game.UNDO()

    def makeMove(self, game):
        game.makeMove()

    def getGameStatus(self, game):
        return game.gameStatus

    def displayResult(self, game):
        return game.printResult()
