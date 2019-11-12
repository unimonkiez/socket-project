import asyncio
from client.game import start

def main(argv=None):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start())
    loop.close()
    return 0
