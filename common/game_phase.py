from enum import Enum as _Enum

class GamePhases(_Enum):
        start = 0
        finished = 1
        tie = 2

class GamePhase:
    def __init__(self, phase, data):
        self._phase = phase
        self._data = data
    
    @classmethod
    def fromString(txt):
        return 1
    
    def toString(self):
        return "1"
