import asyncio
from common.card import Card, CardRanks, CardSuits
from common.game_results import GameResults
from client.response import Response, ResponseTypes
from server.game import Game as ServerGame

serverGame = None

async def start_game(amount):
    # await asyncio.sleep(1)
    global serverGame
    serverGame = ServerGame(20)

    res = Response(
        ResponseTypes.accept,
        {
            "round": 1,
            "amountLeft": serverGame.amount,
            "dealt": serverGame.playersCard
        }
    )

    # res = Response(
    #     ResponseTypes.reject,
    #     {
    #         "messave": "No space",
    #     }
    # )

    return res

async def bet(amount):
    global serverGame
    serverGame.set_bet(amount)

    resDict = {
        "round": serverGame.rounds,
        "dealersCard": serverGame.dealersCard,
        "playersCard": serverGame.playersCard,
        "result": serverGame.result,
        "bet": serverGame.bet,
        "isWar": serverGame.isWar,
        "amountLeft": serverGame.amount,
        "dealt": None
    }

    if (resDict["result"] != GameResults.tie):
        serverGame.nextRound()
        resDict["dealt"] = serverGame.playersCard

    res = Response(
        ResponseTypes.accept,
        resDict
    )

    return res

async def tie_break(isWar):
    global serverGame
    serverGame.tie_break(isWar)
    if (isWar):
        resDict = {
            "round": serverGame.rounds,
            "dealersCard": serverGame.dealersCard,
            "playersCard": serverGame.playersCard,
            "result": serverGame.result,
            "bet": serverGame.bet,
            "originalBet": serverGame.originalBet,
            "isWar": serverGame.isWar,
            "cardsDiscarded": serverGame.cardsDiscarded,
            "amountLeft": serverGame.amount,
            "dealt": None
        }

        if (resDict["result"] != GameResults.tie):
            serverGame.nextRound()
            resDict["dealt"] = serverGame.playersCard

        res = Response(
            ResponseTypes.accept,
            resDict
        )
    else:
        resDict = {
            "round": serverGame.rounds,
            "dealers": serverGame.dealersCard,
            "result": GameResults.playerSurrender,
            "bet": serverGame.bet,
            "originalBet": serverGame.originalBet,
            "isWar": serverGame.isWar,
            "playerEarn": serverGame.playerEarn,
            "dealerEarn": serverGame.dealerEarn,
            "amountLeft": serverGame.amount,
            "dealt": None
        }
        serverGame.nextRound()
        resDict["dealt"] = serverGame.playersCard

        res = Response(
            ResponseTypes.accept,
            resDict
        )

    return res

def start_game_sync(amount): 
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(start_game(amount))

def bet_sync(amount): 
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(bet(amount))

def tie_break_sync(isWar): 
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(tie_break(isWar))
