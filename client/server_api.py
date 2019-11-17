import asyncio
from common.card import Card, CardRanks, CardSuits
from common.game_results import GameResults
from client.response import Response, ResponseTypes
from server.game import Game as ServerGame

serverGame = None

async def start_game(amount):
    # await asyncio.sleep(1)

    serverGame = ServerGame(amount)

    res = Response(
        ResponseTypes.accept,
        {
            "round": 1,
            "amountLeft": 50,
            "dealt": serverGame.playerCard
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
    serverGame.setBet(amount)

    resDict = {
        "round": serverGame.round,
        "dealersCard": serverGame.dealersCard,
        "playersCard": serverGame.playersCard,
        "result": serverGame.result,
        "originalBet": serverGame.bet,
        "amountLeft": 50,
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
    serverGame.tie_break(isWar)
    if (isWar):
        print("TODO: war")
        # res = Response(
        #     ResponseTypes.accept,
        #     {
        #         "round": 1,
        #         "dealers": Card(CardRanks.num3, CardSuits.hearts),
        #         "result": GameResults.tie,
        #         "dealt": Card(CardRanks.ace, CardSuits.hearts)
        #     }
        # )
    else:
        resDict = {
            "round": serverGame.round,
            "dealers": serverGame.dealersCard,
            "result": GameResults.playerSurrender,
            "originalBet": serverGame.bet,
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
