from server.server_manager import ServerManager
from time import sleep

def main(argv=None):
    serverManager = ServerManager()
    serverManager.start()

    # Server manager starts another thread, so keep main thread alive to catch KeyboardInterrupt
    try:
        while True:
            sleep(200)
    except KeyboardInterrupt:
        serverManager.terminate()
        raise

    return 0

