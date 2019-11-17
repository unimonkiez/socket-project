import random
from common.card import Card, CardCompare
from common.game_results import GameResults

class Game:
    def __init__(self, amount):
        self.amount = amount
        self._deck = Card.getRandomDeck()
        self._rounds = []
        self.nextRound()
    
    def nextRound(self):
        self._rounds.append({
            "dealersCard": None,
            "playersCard": self._deck.pop(),
            "result": None,
            "bet": None,
            "playerEarn": None,
            "dealerEarn": None
        })
        self.playerCard = self._deck.pop()
        self.dealerCard = None
    
    @property
    def rounds(self):
        return len(self._rounds)

    @property
    def playersCard(self):
        return len(self._rounds[-1]["playersCard"])

    @property
    def dealersCard(self):
        return len(self._rounds[-1]["dealersCard"])

    @property
    def result(self):
        return len(self._rounds[-1]["result"])

    @property
    def bet(self):
        return len(self._rounds[-1]["bet"])
        
    @property
    def playerEarn(self):
        return len(self._rounds[-1]["playerEarn"])

    @property
    def dealerEarn(self):
        return len(self._rounds[-1]["dealerEarn"])
  
    def setBet(self, bet):
        self._rounds[-1]["bet"] = bet
        self._rounds[-1]["dealersCard"] = self._deck.pop()

        result = None
        cardCompare = self.playerCard.compare(self.dealerCard)
        if (cardCompare == CardCompare.wins):
            result = GameResults.playerWin
        elif (cardCompare == CardCompare.loses):
            result = GameResults.dealerWin
            self.amount = self.amount - self._rounds[-1]["bet"]
        else:
            result = GameResults.tie
        
        self._rounds[-1]["result"] = result
    
    def tie_break(self, isWar):
        if (isWar):
            print("TODO: war")
        else:
            lastRound = self._rounds[-1]
            bet = lastRound["bet"]
            lastRound["playerEarn"] = bet / 2
            lastRound["dealerEarn"] = bet / 2
            self.amount = self.amount - lastRound["dealerEarn"]
            

    
