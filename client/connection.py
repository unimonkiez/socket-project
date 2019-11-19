from common.event import get_do_request as _get_do_request
from common.port_manager import LISTENER_PORT
from common.response import Response, ResponseTypes

class _Connection:
    def __init__(self, port):
        self._port = port
        self._do_request = None
    
    def do_request(self, data, sucessHandler, rejectHandler):
        def reqHandler(resDict):
            res = Response.fromDict(resDict)
            res.handle(sucessHandler, rejectHandler)

        try:
            if (self._do_request == None):
                self._do_request = _get_do_request(self._port)
            self._do_request(data, reqHandler)
        except ConnectionRefusedError as err:
            rejectHandler({
                "message": str(err)
            })
        except ConnectionResetError as err:
            rejectHandler({
                "message": str(err)
            })
        except Exception:
            raise

_mainConnection = _Connection(LISTENER_PORT)

def get_connection(data, sucessHandler, rejectHandler):
    def reqHander(res):
        port = res["port"]
        sucessHandler(_Connection(port), res["data"])

    _mainConnection.do_request(data, reqHander, rejectHandler)

