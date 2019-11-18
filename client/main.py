from client.game import Game
from common.connection import do_request

def main(argv=None):
    do_request(
        20000,
        {
            "x": 3
        },
        sucess
        )

    game = Game()
    game.start()
    return 0

def sucess(data):
    print('Received ', data)   

