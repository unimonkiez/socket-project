from common.event import do_request as _do_request
from common.port_manager import LISTENER_PORT
from common.response import Response, ResponseTypes

class _Connection:
    def __init__(self, port):
        self._port = port
    
    def do_request(self, data, sucessHandler, rejectHandler):
        def reqHandler(resDict):
            res = Response.fromDict(resDict)
            res.handle(sucessHandler, rejectHandler)

        try:
            _do_request(self._port, data, reqHandler)
        except ConnectionRefusedError as err:
            rejectHandler({
                "message": str(err)
            })

_mainConnection = _Connection(LISTENER_PORT)

def get_connection(data, sucessHandler, rejectHandler):
    def reqHander(res):
        port = res["port"]
        sucessHandler(_Connection(port), res["data"])

    _mainConnection.do_request(data, reqHander, rejectHandler)

