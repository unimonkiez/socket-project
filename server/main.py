from server.server_manager import ServerManager

def main(argv=None):
    serverManager = ServerManager()
    serverManager.start()

    return 0

