from enum import Enum

""" EnumS """


class GameStatus(Enum):
    INPROGESS = 1
    ENDED = 2
    DRAW = 3


class CellState(Enum):
    EMPTY = 1
    FILLED = 2
    BLOCKED = 3


class PlayerType(Enum):
    HUMAN = 1
    BOT = 2
    GUEST = 3


class DifficultyLevel(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
