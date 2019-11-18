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

    @classmethod
    def fromStr(cls, txt):
        switcher = {
            "a": CardRanks.ace,
            "2": CardRanks.num2,
            "3": CardRanks.num3,
            "4": CardRanks.num4,
            "5": CardRanks.num5,
            "6": CardRanks.num6,
            "7": CardRanks.num7,
            "8": CardRanks.num8,
            "9": CardRanks.num9,
            "10": CardRanks.num10,
            "j": CardRanks.jack,
            "q": CardRanks.queen,
            "k": CardRanks.king
        }
        return switcher.get(txt)


    def toStr(self):
        return self.text
        

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
    def fromDict(cls, someDict):
        rank = CardRanks.fromStr(someDict["rank"])
        suit = CardSuits(someDict["suit"])
        
        return Card(rank, suit)
    
    def toDict(self):
        return {
            "rank": self.rank.toStr(),
            "suit": self.suit.value
        }
      
    def compare(self, card):
          rankNumber = self.rank.number
          compareRankNumber = card.rank.number

          if (rankNumber == compareRankNumber):
                return CardCompare.ties
          elif (rankNumber > compareRankNumber):
                return CardCompare.wins
          else:
                return CardCompare.loses
      
    def toNiceString(self):
        return "{} of {}".format(self.rank.displayName.capitalize(), self.suit.name.capitalize())
