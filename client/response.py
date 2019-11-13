from enum import Enum as _Enum

class ResponseTypes(_Enum):
        accept = 1
        reject = 2

class Response:
    def __init__(self, type, data):
        self.type = type
        self.data = data
    
    async def handle(self, res, rej):
        if (self.type == ResponseTypes.accept):
            await res(self.data)
        elif (self.type == ResponseTypes.reject):
            await rej(self.data)