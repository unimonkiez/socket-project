import asyncio
from common.card import Card, CardRanks, CardSuits
from common.game_results import GameResults
from client.response import Response, ResponseTypes
from server.game import Game as ServerGame

serverGame = None

async def start_game(amount):
    # await asyncio.sleep(1)
    global serverGame
    serverGame = ServerGame(amount)

    res = Response(
        ResponseTypes.accept,
        {
            "round": 1,
            "amountLeft": serverGame.amount,
            "originalAmount": serverGame.originalAmount,
            "dealt": serverGame.playersCard
        }
    )

    # res = Response(
    #     ResponseTypes.reject,
    #     {
    #         "message": "No space",
    #     }
    # )

    return res

async def play_again(isPlayingAgain):
    global serverGame

    if (isPlayingAgain):
        serverGame.reshuffle()

    res = Response(
        ResponseTypes.accept,
        {
            "round": 1,
            "amountLeft": serverGame.amount,
            "originalAmount": serverGame.originalAmount,
            "dealt": serverGame.playersCard
        }
    )

    return res

def _create_res():
    global serverGame

    resDict = {
        "round": serverGame.rounds,
        "dealersCard": serverGame.dealersCard,
        "playersCard": serverGame.playersCard,
        "result": serverGame.result,
        "bet": serverGame.bet,
        "originalBet": serverGame.originalBet,
        "playerEarn": serverGame.playerEarn,
        "dealerEarn": serverGame.dealerEarn,
        "isWar": serverGame.isWar,
        "autoSurrender": serverGame.autoSurrender,
        "cardsDiscarded": serverGame.cardsDiscarded,
        "amountLeft": serverGame.amount,
        "originalAmount": serverGame.originalAmount,
        "ended": serverGame.ended,
        "dealt": None
    }

    if (resDict["result"] != GameResults.tie):
        serverGame.nextRound()
        resDict["ended"] = serverGame.ended
        resDict["dealt"] = serverGame.playersCard

    res = Response(
        ResponseTypes.accept,
        resDict
    )

    return res

async def bet(amount):
    global serverGame
    serverGame.set_bet(amount)

    return _create_res()

async def tie_break(isWar):
    global serverGame
    serverGame.tie_break(isWar)

    return _create_res()

def start_game_sync(amount): 
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(start_game(amount))

def play_again_sync(amount): 
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(play_again(amount))

def bet_sync(amount): 
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(bet(amount))

def tie_break_sync(isWar): 
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(tie_break(isWar))
