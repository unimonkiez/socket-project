from enum import Enum as _Enum

class CardSuits(_Enum):
        clubs = "c"
        diamonds = "d"
        hearts = "h"
        spades = "s"

class CardRanks(_Enum):
        ace = "a"
        num2 = "2"
        num3 = "3"
        num4 = "4"
        num5 = "5"
        num6 = "6"
        num7 = "7"
        num8 = "8"
        num9 = "9"
        num10 = "10"
        jack = "j"
        queen = "q"
        king = "k"

class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
    
    @classmethod
    def fromString(str):
        