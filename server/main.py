import sys
from common.connection import listen
from time import sleep

def main(argv=None):
    if argv is None:
        argv = sys.argv

    print("Server")
    
    terminate = listen(
        20000,
        message
        )
    
    sleep(2)

    terminate()

    # terminate = listen(
    #     20000,
    #     message
    #     )

    return 0

def message(data):
    print('Received ', data)

    return {
        "y": 5
    }
