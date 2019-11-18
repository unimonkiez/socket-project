from client.game import Game

def main(argv=None):
    game = Game()
    game.start()
    return 0

def sucess(data):
    print('Received ', data)   

