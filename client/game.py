from client.server_api import start_game


class Game:
    def __init__(self):
        self._amount = None

    async def start(self):
        while (self._amount == None):
            txt = input("Please enter amount of cash ($) to convert to chips and start session:\n")
            try:
                amount = int(txt)
                if (amount <= 0):
                    print("Amount should be positive, \"{}\" is invalid, try again\n".format(amount))
                else:
                    self._amount = amount
            except:
                print("\"{}\" is an invalid number, try again\n".format(txt))

        res = await start_game(self._amount)
        await res.handle(self._start_success, self._start_reject)

    async def _start_success(self, data): 
        await self._make_bet()

    async def _start_reject(self, data): 
        txt = input("Failed with message: \n{}\nPress Enter to retry, \"q\" to quit\n".format(data.message))
        if (txt != "q"):
            self._amount = None
            await self.start()

    async def _make_bet(self):
        print("sucess")