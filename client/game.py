import client.server_api as server_api
from common.game_results import GameResults
from common.noop import noop

class Game:
    def __init__(self):
        self._connection = None

    def start(self):
        amount = self._get_amount()
        server_api.start_game_sync(amount, self._start_success, self._reject_start_again)

    def _start_success(self, connection, res):
        self._connection = connection
        self._dealt(res)

    def _dealt(self, res):
        bet = self._get_bet(res)
        server_api.bet_sync(self._connection, bet, self._bet_success, self._reject_start_again)

    def _reject_start_again(self, res): 
        txt = input("Failed with message: \n{}\nPress Enter to retry, \"q\" to quit\n".format(res["message"]))
        if (txt != "q"):
            self.start()

    def _bet_success(self, res):
        self._process_result(res)

    def _process_result(self, res):
        result = res["result"]
        self._print_round_details(res)
        if (self._validate_game_not_ended(res)):
            if (result == GameResults.tie):
                self._tie_break(res)
            else:
                self._round_done(res)

    def _tie_break(self, res): 
        isWar = self._get_is_war(res)
        server_api.tie_break_sync(self._connection, isWar, self._bet_success, self._reject_start_again)
    
    def _tie_break_success(self, res):
        self._result = res["result"]
        self._print_round_details(res)
    
    def _play_again_sucess(self, res):
        self._dealt(res)

    def _print_round_details(self, res):
        if (res["result"] == GameResults.playerSurrender):
            reason = ""
            if (res["autoSurrender"]):
                reason = " (Because there weren't enough cards for war)"
            print(
                "\nRound {} tie breaker:\nPlayer surrendered!{}\nThe bet: {}$\nDealer won: {}$\nPlayer won: {}$"
                .format(res["round"], reason, res["bet"], res["dealerEarn"], res["playerEarn"])
            )
        else:
            secondLine = ""
            lastLine = ""
            
            if (res["isWar"]):
                secondLine = "Going to war!\n{} cards were discarded.\nOriginal bet: {}$\nNew bet: {}$\n".format(res["cardsDiscarded"], res["originalBet"], res["bet"])
            if (res["result"] == GameResults.playerWin):
                lastLine = "Player won {}$\n".format(res["bet"])
            elif (res["result"] == GameResults.dealerWin):
                lastLine = "Dealer won {}$\n".format(res["bet"])
            else:
                lastLine = "The bet is {}$\n".format(res["bet"])

            print(
                "\nThe result of round {} is {}!\n{}Dealer’s card: {},\nPlayer’s card: {}{}"
                .format(res["round"], res["result"].displayName, secondLine, res["dealersCard"].toNiceString(), res["playersCard"].toNiceString(), lastLine)
            )
    
    def _validate_game_not_ended(self, res):
        ended = res["ended"]
        if (ended):
            print("The game has ended!\nPlayer won: {}$\n".format(res["amountLeft"] - res["originalAmount"]))
            playAgain = self._get_play_again()
            if (playAgain):
                server_api.play_again_sync(self._connection, playAgain, self._play_again_sucess, self._reject_start_again)
            else:
                server_api.play_again_sync(self._connection, playAgain, noop, noop)
        
        return ended == False
            
    def _round_done(self, res):
        self._dealt(res)

    def _get_amount(self):
        amount = None
        while (amount == None):
            txt = input("\nPlease enter amount of cash ($) to convert to chips and start session:\n")
            try:
                num = int(txt)
                if (num <= 0):
                    print("Amount should be positive, \"{}\" is invalid, try again\n".format(num))
                else:
                    amount = num
            except:
                print("\"{}\" is an invalid number, try again\n".format(txt))
        
        return amount

    def _get_bet(self, res):
        amount = res["amountLeft"]
        bet = None
        while (bet == None):
            txt = input("\nYou got dealt the card {}, how much you want to bet? ({}$ left)\n".format(res["dealt"].toNiceString(), res["amountLeft"]))
            try:
                num = int(txt)
                if (num <= 0):
                    print("Bet should be positive, \"{}\" is invalid, try again\n".format(bet))
                elif (num > amount):
                    print("Don't have enough chips! you have {}$ in chips, {}$ is invalid, try again\n".format(amount, num))
                else:
                    bet = num
            except:
                print("\"{}\" is an invalid number, try again\n".format(txt))
        
        return bet

    def _get_play_again(self):
        txt = input("Continue? (Y/n)\n")
        return txt != "n"

    def _get_is_war(self, res):
        amount = res["amountLeft"]
        bet = res["bet"]
        if (bet * 2 > amount):
            print("Don't have enough chips to go to war! surrenders")
            return False
        else:
            txt = input("Go to war? (Y/n)\n")
            return txt != "n"
    
        
