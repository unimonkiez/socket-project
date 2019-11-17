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
        if (len(self._deck) < 2):
            raise Exception("Not enough cards for another game, ended\n")
        self._rounds.append({
            "dealersCard": None,
            "playersCard": self._deck.pop(),
            "result": None,
            "bet": None,
            "originalBet": None,
            "playerEarn": None,
            "dealerEarn": None,
            "isWar": False,
            "cardsDiscarded": 0
        })
    
    @property
    def rounds(self):
        return len(self._rounds)

    @property
    def playersCard(self):
        return self._rounds[-1]["playersCard"]

    @property
    def dealersCard(self):
        return self._rounds[-1]["dealersCard"]

    @property
    def result(self):
        return self._rounds[-1]["result"]

    @property
    def bet(self):
        return self._rounds[-1]["bet"]

    @property
    def isWar(self):
        return self._rounds[-1]["isWar"]

    @property
    def originalBet(self):
        return self._rounds[-1]["originalBet"]

    @property
    def dealerEarn(self):
        return self._rounds[-1]["dealerEarn"]
        
    @property
    def playerEarn(self):
        return self._rounds[-1]["playerEarn"]

    @property
    def cardsDiscarded(self):
        return self._rounds[-1]["cardsDiscarded"]
  
    def set_bet(self, bet):
        if (bet > self.amount):
            raise Exception("Don't have enough chips! you have {}$ in chips, {}$ is invalid, try again\n".format(self.amount, bet))

        self._rounds[-1]["bet"] = bet

        self._rounds[-1]["dealersCard"] = self._deck.pop()
        # For always to tie, uncomment next line
        # self._rounds[-1]["dealersCard"] = self.playersCard 

        result = None
        cardCompare = self.playersCard.compare(self.dealersCard)
        if (cardCompare == CardCompare.wins):
            result = GameResults.playerWin
            self.amount = self.amount + self._rounds[-1]["bet"]
        elif (cardCompare == CardCompare.loses):
            result = GameResults.dealerWin
            self.amount = self.amount - self._rounds[-1]["bet"]
        else:
            result = GameResults.tie
        
        if (cardCompare != CardCompare.ties and len(self._deck) < 5):
            self.tie_break(False)
            raise Exception("Not enough cards for tie breaker, ended with no war\n")
        
        self._rounds[-1]["result"] = result
    
    def tie_break(self, isWar):
        lastRound = self._rounds[-1]
        bet = lastRound["bet"]
        if (isWar):
            self._deck.pop()
            self._deck.pop()
            self._deck.pop()
            lastRound["cardsDiscarded"] = 3
            lastRound["isWar"] = True
            lastRound["playersCard"] = self._deck.pop()
            if (lastRound["originalBet"] == None):
                lastRound["originalBet"] = bet

            self.set_bet(bet * 2)
        else:
            lastRound["playerEarn"] = bet / 2
            lastRound["dealerEarn"] = bet / 2
            self.amount = self.amount - lastRound["dealerEarn"]
            

    
