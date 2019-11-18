from enum import Enum as _Enum

class ResponseTypes(_Enum):
        accept = 1
        reject = 2

class Response:
    def __init__(self, resType: ResponseTypes, data: dict):
        self.type = resType
        self.data = data
    
    def toDict(self):
        return {
            "type": self.type.value,
            "data": self.data
        }
    
    @classmethod
    def fromDict(cls, someDict):
        return Response(ResponseTypes(someDict["type"]), someDict["data"])

    
    def handle(self, res, rej):
        if (self.type == ResponseTypes.accept):
            res(self.data)
        elif (self.type == ResponseTypes.reject):
            rej(self.data)