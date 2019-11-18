from common.event import listen
from server.game import Game
from common.client_api import ClientApis
from common.game_results import GameResults
from common.response import Response, ResponseTypes

class ClientManager:
    def __init__(self, port, terminate, initialData):
        self.terminate = terminate
        self._port = port
        self._game = Game(initialData["amount"])

    def start(self):
        listen(self._port, self._listener_handler)
        print("Client started on port {}\n".format(self._port))

    @property
    def initialResponse(self):
        return {
            "round": self._game.rounds,
            "amountLeft": self._game.amount,
            "originalAmount": self._game.originalAmount,
            "dealt": self._game.playersCard.toDict()
        }
    
    def _listener_handler(self, data):
        switcher = {}
        switcher[ClientApis.tie_break.value] = self._tie_break_handler
        switcher[ClientApis.bet.value] = self._bet_handler
        switcher[ClientApis.play_again.value] = self._play_again_handler

        res = None

        handler = switcher.get(data["api"])
        resData = handler(data["data"])

        res = Response(ResponseTypes.accept, resData)
        # try:
            
        # except Exception as err:
        #     res = Response(ResponseTypes.reject, {
        #         "message": str(err)
        #     })
        
        return res.toDict()
    
    def _bet_handler(self, data):
        bet = data["bet"]
        print("bettt", bet)
        self._game.set_bet(bet)

        return self._game_progress_res()

    def _tie_break_handler(self, data): 
        isWar = data["isWar"]
        self._game.tie_break(isWar)

        return self._game_progress_res()

    def _play_again_handler(self, data):
        isPlayingAgain = data["isPlayingAgain"]
        if (isPlayingAgain):
            self._game.reshuffle()
            return self.initialResponse
        else:
            self.terminate()
            return {}
        

    def _game_progress_res(self):
        res = {
            "round": self._game.rounds,
            "dealersCard": self._game.dealersCard.toDict(),
            "playersCard": self._game.playersCard.toDict(),
            "result": self._game.result.toStr(),
            "bet": self._game.bet,
            "originalBet": self._game.originalBet,
            "playerEarn": self._game.playerEarn,
            "dealerEarn": self._game.dealerEarn,
            "isWar": self._game.isWar,
            "autoSurrender": self._game.autoSurrender,
            "cardsDiscarded": self._game.cardsDiscarded,
            "amountLeft": self._game.amount,
            "originalAmount": self._game.originalAmount,
            "ended": self._game.ended,
            "dealt": None
        }

        if (res["result"] != GameResults.tie):
            self._game.nextRound()
            res["ended"] = self._game.ended
            res["dealt"] = self._game.playersCard.toDict()

        return res

