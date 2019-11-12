import asyncio
from client.response import Response, ResponseTypes

async def start_game(amount):
    await asyncio.sleep(1)

    res = Response(ResponseTypes.accept, 1)

    return res