import asyncio
from common.card import Card, CardRanks, CardSuits
from common.game_results import GameResults
from client.response import Response, ResponseTypes


async def start_game(amount):
    # await asyncio.sleep(1)

    res = Response(
        ResponseTypes.accept,
        {
            "round": 1,
            "amountLeft": 50,
            "dealt": Card(CardRanks.ace, CardSuits.hearts)
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
    res = Response(
        ResponseTypes.accept,
        {
            "round": 1,
            "dealersCard": Card(CardRanks.num3, CardSuits.hearts),
            "playersCard": Card(CardRanks.ace, CardSuits.hearts),
            "result": GameResults.tie,
            "originalBet": 20,
            "amountLeft": 50,
            "dealt": Card(CardRanks.ace, CardSuits.hearts)
        }
    )

    return res

async def tie_break(isWar):
    if (isWar):
        res = Response(
            ResponseTypes.accept,
            {
                "round": 1,
                "dealers": Card(CardRanks.num3, CardSuits.hearts),
                "result": GameResults.tie,
                "dealt": Card(CardRanks.ace, CardSuits.hearts)
            }
        )
    else:
        res = Response(
            ResponseTypes.accept,
            {
                "round": 1,
                "dealers": Card(CardRanks.num3, CardSuits.hearts),
                "result": GameResults.playerSurrender,
                "originalBet": 50,
                "playerEarn": 25,
                "dealerEarn": 25,
                "amountLeft": 100,
                "dealt": Card(CardRanks.ace, CardSuits.hearts)
            }
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
