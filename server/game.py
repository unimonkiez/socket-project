import random
import math
from common.card import Card, CardCompare
from common.game_results import GameResults

class Game:
    def __init__(self, amount):
        if (isinstance(amount, int) == False or amount <= 0):
            raise Exception("\"{}\" is an invalid number, should be positive int".format(amount))

        self.amount = amount
        self.originalAmount = amount
        self.ended = False
        self._deck = Card.getRandomDeck()
        self._rounds = []
        self.nextRound()

        # For running deck low on start on comment next lines
        # for x in range(0, 48):
        #     self._deck.pop()
        # print("{} cards left".format(len(self._deck)))
    
    @property
    def rounds(self):
        return len(self._rounds)
        
    @property
    def _last_round(self):
        return self._rounds[-1]

    @property
    def playersCard(self):
        return self._last_round["playersCard"]

    @property
    def dealersCard(self):
        return self._last_round["dealersCard"]

    @property
    def result(self):
        return self._last_round["result"]

    @property
    def bet(self):
        return self._last_round["bet"]

    @property
    def isWar(self):
        return self._last_round["isWar"]

    @property
    def originalBet(self):
        return self._last_round["originalBet"]

    @property
    def dealerEarn(self):
        return self._last_round["dealerEarn"]
        
    @property
    def playerEarn(self):
        return self._last_round["playerEarn"]

    @property
    def autoSurrender(self):
        print(self._last_round["autoSurrender"])
        return self._last_round["autoSurrender"]

    @property
    def cardsDiscarded(self):
        return self._last_round["cardsDiscarded"]

    def nextRound(self):
        self._validate_game()
        if (len(self._deck) < 2 or self.amount == 0):
            self.ended = True
        else:
            self._rounds.append({
                "dealersCard": None,
                "playersCard": self._deck.pop(),
                "result": None,
                "bet": None,
                "originalBet": None,
                "playerEarn": None,
                "dealerEarn": None,
                "isWar": False,
                "cardsDiscarded": 0,
                "autoSurrender": False
            })

    def set_bet(self, bet):
        self._validate_game()
        if (isinstance(bet, int) == False or bet <= 0):
            raise Exception("\"{}\" is an invalid number, should be positive int".format(bet))
        elif (bet > self.amount):
            raise Exception("Game has {}$ in chips, {}$ is invalid".format(self.amount, bet))

        self._last_round["bet"] = bet

        self._last_round["dealersCard"] = self._deck.pop()
        # For always to tie, uncomment next line
        # self._last_round["dealersCard"] = self.playersCard 

        result = None
        cardCompare = self.playersCard.compare(self.dealersCard)
        if (cardCompare == CardCompare.wins):
            result = GameResults.playerWin
            self.amount = self.amount + self._last_round["bet"]
        elif (cardCompare == CardCompare.loses):
            result = GameResults.dealerWin
            self.amount = self.amount - self._last_round["bet"]
        else:
            result = GameResults.tie
        
        self._last_round["result"] = result

        if (cardCompare == CardCompare.ties and len(self._deck) < 5):
            self.tie_break(False)
            self._last_round["autoSurrender"] = True
            
    def tie_break(self, isWar):
        self._validate_game()
        if (isinstance(isWar, bool) == False):
            raise Exception("\"{}\" is an invalid bool".format(isWar))

        bet = self._last_round["bet"]
        if (isWar):
            self._deck.pop()
            self._deck.pop()
            self._deck.pop()
            self._last_round["cardsDiscarded"] = 3
            self._last_round["isWar"] = True
            self._last_round["playersCard"] = self._deck.pop()
            if (self._last_round["originalBet"] == None):
                self._last_round["originalBet"] = bet

            self.set_bet(bet * 2)
        else:
            self._last_round["result"] = GameResults.playerSurrender
            self._last_round["playerEarn"] = math.ceil(bet / 2)
            self._last_round["dealerEarn"] = math.floor(bet / 2)
            self.amount = self.amount - self._last_round["dealerEarn"]
    
    def _validate_game(self):
        if (self.ended):
            raise Exception("Game have ended, go home!")

    
