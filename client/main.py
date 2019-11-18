from client.game import Game
from client.connection import get_connection

def main(argv=None):
    game = Game()
    game.start()
    
    return 0

def sucess(connection, data):
    print('Received ', data)   

def reject(data):
    print('Received ', data)   

