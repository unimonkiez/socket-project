from common.response import Response
from client.connection import get_connection
from common.card import Card
from common.game_results import GameResults
from common.client_api import ClientApis

def start_game_sync(amount, successHandler, rejectHandler): 
    def middlewareSucessHandler(con, res):
        newRes = res
        newRes["dealt"] = Card.fromDict(res["dealt"])
        successHandler(con, newRes)

    get_connection({
        "amount": amount
    }, middlewareSucessHandler, rejectHandler)

def play_again_sync(connection, isPlayingAgain, successHandler, rejectHandler):
    def middlewareSucessHandler(res):
        newRes = res
        if (isPlayingAgain):
            newRes["dealt"] = Card.fromDict(res["dealt"])
        successHandler(newRes)


    connection.do_request({
        "api": ClientApis.play_again.value,
        "data": {
            "isPlayingAgain": isPlayingAgain
        }
    }, middlewareSucessHandler, rejectHandler)

def bet_sync(connection, bet, successHandler, rejectHandler): 
    def middlewareSucessHandler(res):
        newRes = res
        newRes["result"] = GameResults.fromStr(res["result"])
        newRes["dealersCard"] = Card.fromDict(res["dealersCard"])
        newRes["playersCard"] = Card.fromDict(res["playersCard"])
        if (res["dealt"] != None):
            newRes["dealt"] = Card.fromDict(res["dealt"])
        successHandler(newRes)

    connection.do_request({
        "api": ClientApis.bet.value,
        "data": {
            "bet": bet
        }
    }, middlewareSucessHandler, rejectHandler)


def tie_break_sync(connection, isWar, successHandler, rejectHandler): 
    def middlewareSucessHandler(res):
        newRes = res
        newRes["result"] = GameResults.fromStr(res["result"])
        newRes["dealersCard"] = Card.fromDict(res["dealersCard"])
        newRes["playersCard"] = Card.fromDict(res["playersCard"])
        if (res["dealt"] != None):
            newRes["dealt"] = Card.fromDict(res["dealt"])
        successHandler(newRes)

    connection.do_request({
        "api": ClientApis.tie_break.value,
        "data": {
            "isWar": isWar
        }
    }, middlewareSucessHandler, rejectHandler)

