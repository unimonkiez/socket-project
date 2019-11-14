from enum import Enum as _Enum
import random

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

class CardSuits(_Enum):
        clubs = "c"
        diamonds = "d"
        hearts = "h"
        spades = "s"

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @classmethod
    def getRandomDeck():
        deck = []
        for rank in (CardRanks):
              for suit in (CardSuits):
                    deck.append(Card(rank, suit))
        
        random.shuffle(deck)

        return deck
    
    @classmethod
    def fromString(txt):
        txtLength = len(txt);
        rank = None
        suit = None
        if (txtLength == 2):
          rank = txt[0:1]
          suit = txt[1:2]
        elif (txtLength == 3):
          rank = txt[0:2]
          suit = txt[2:3]
        
        return Card(suit, rank)
    
    def toString(self):
        return "{}{}".format(self._rank.value, self._suit.value)
      
    def toNiceString(self):
        return "{} {}".format(self._rank.name.replace("num", "Number ").capitalize(), self._suit.name.capitalize())
