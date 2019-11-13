import asyncio
from client.response import Response, ResponseTypes

async def start_game(amount):
    await asyncio.sleep(1)

    res = Response(ResponseTypes.accept, 1)
    # res = Response(ResponseTypes.reject, 
    #     type('',(object,),{"message": "No space"})()
    # )

    return res