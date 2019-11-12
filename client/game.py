from client.server_api import start_game

async def start():
    amount = input("Please enter amount of cash ($) to convert to chips and start session:\n")
    res = await start_game(amount)
    res.handle(success, success)

def success(): 
    print("sucess")
