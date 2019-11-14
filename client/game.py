import client.server_api as server_api
from common.game_results import GameResults


class Game:
    def start(self):
        amount = self._get_amount()
        req = server_api.start_game_sync(amount)
        req.handle(self._start_success, self._start_again)

    def _start_success(self, res):
        self._dealt(res)

    def _dealt(self, res):
        bet = self._get_bet(res)
        req = server_api.bet_sync(bet)
        req.handle(self._bet_success, self._start_again)

    def _start_again(self, res): 
        txt = input("Failed with message: \n{}\nPress Enter to retry, \"q\" to quit\n".format(res["message"]))
        if (txt != "q"):
            self.start()


    def _bet_success(self, res):
        self._process_result(res)

    def _process_result(self, res):
        result = res["result"]
        if (result == GameResults.tie):
            self._tie_break()
        else:
          self._print_round_details(res)
          self._round_done(res)

    def _tie_break(self): 
        isWar = self._get_is_war()
        req = server_api.tie_break_sync(isWar)
        req.handle(self._bet_success, self._start_again)
    
    def _tie_break_success(self, res):
        self._result = res["result"]
        self._print_round_details(res)


    def _print_round_details(self, res):
        if (res["result"] == GameResults.playerSurrender):
            print(
                "Round {} tie breaker:\nPlayer surrendered!\nThe bet: {}$\nDealer won: {}$\nPlayer won: {}$\n"
                .format(res["round"], res["originalBet"], res["dealerEarn"], res["playerEarn"])
            )
        else:
            print(
                "The result of round {} is {}!\nDealer won: {}$\nDealer’s card: {},\nPlayer’s card: {}\n"
                .format(res["round"], res["result"].displayName, res["originalBet"], res["dealersCard"].toNiceString(), res["playersCard"].toNiceString())
            )
    
    def _round_done(self, res):
        self._dealt(res)

    def _get_amount(self):
        amount = None
        while (amount == None):
            txt = input("Please enter amount of cash ($) to convert to chips and start session:\n")
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
            txt = input("You got dealt the card {}, how much you want to bet?\n".format(res["dealt"].toNiceString()))
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

    def _get_is_war(self):
        txt = input ("Go to war?(Y/n)\n")
        return txt != "n"
    
        
