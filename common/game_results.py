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

    def toStr(self):
        return str(self.value.number)

    @classmethod
    def fromStr(cls, txt):
        switcher = {
            "0": GameResults.tie,
            "1": GameResults.dealerWin,
            "2": GameResults.playerWin,
            "4": GameResults.playerSurrender
        }

        return switcher.get(txt)

    tie = GameResult(0, 'a tie')
    dealerWin = GameResult(1, 'dealer won')
    playerWin = GameResult(2, 'player won')
    playerSurrender = GameResult(4, 'player surrendered')