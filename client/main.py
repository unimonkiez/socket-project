import asyncio
from client.game import Game

def main(argv=None):
    game = Game()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(game.start())
    loop.close()
    return 0
