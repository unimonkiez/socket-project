from enum import Enum
import random
from collections import namedtuple

CardRank = namedtuple('CardRank', ['text', 'number', 'displayName'])

class CardRanks(Enum):
    @property
    def text(self):
        return self.value.text

    @property
    def number(self):
        return self.value.number

    @property
    def displayName(self):
        return self.value.displayName

    ace = CardRank("a", 13, "ace")
    num2 = CardRank("2", 1, "2")
    num3 = CardRank("3", 2, "3")
    num4 = CardRank("4", 3, "4")
    num5 = CardRank("5", 4, "5")
    num6 = CardRank("6", 5, "6")
    num7 = CardRank("7", 6, "7")
    num8 = CardRank("8", 7, "8")
    num9 = CardRank("9", 8, "9")
    num10 = CardRank("10", 9, "10")
    jack = CardRank("j", 10, "jack")
    queen = CardRank("q", 11, "queen")
    king = CardRank("k", 12, "king")

class CardSuits(Enum):
        clubs = "c"
        diamonds = "d"
        hearts = "h"
        spades = "s"

class CardCompare(Enum):
        wins = 0
        loses = 1
        ties = 2

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @classmethod
    def getRandomDeck(cls):
        deck = []
        for rank in (CardRanks):
              for suit in (CardSuits):
                    deck.append(Card(rank, suit))
        
        random.shuffle(deck)

        return deck
    
    @classmethod
    def fromString(cls, txt):
        txtLength = len(txt)
        rank = None
        suit = None
        if (txtLength == 2):
          rank = txt[0:1]
          suit = txt[1:2]
        elif (txtLength == 3):
          rank = txt[0:2]
          suit = txt[2:3]
        
        return Card(suit, rank)
      
    def compare(self, card):
          rankNumber = self.rank.number
          compareRankNumber = card.rank.number

          if (rankNumber == compareRankNumber):
                return CardCompare.ties
          elif (rankNumber > compareRankNumber):
                return CardCompare.wins
          else:
                return CardCompare.loses
    
    def toString(self):
        return "{}{}".format(self.rank.text, self.suit.text)
      
    def toNiceString(self):
        return "{} of {}".format(self.rank.displayName.capitalize(), self.suit.name.capitalize())
