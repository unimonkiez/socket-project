from enum import Enum
from collections import namedtuple

GameResult = namedtuple('GameResult', ['number', 'displayName'])

class GameResults(Enum):
    @property
    def displayName(self):
        return self.value.displayName

    @property
    def key(self):
        return self.value.number

    tie = GameResult(0, 'a tie')
    dealerWin = GameResult(1, 'dealer won')
    playerWin = GameResult(2, 'player won')
    playerSurrender = GameResult(4, 'player surrendered')