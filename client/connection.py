from common.event import do_request as _do_request
from common.port_manager import LISTENER_PORT

class Connection:
    def __init__(self, port):
        self._port = port
    
    def do_request(self, data, handler):
        _do_request(self._port, data, handler)

_mainConnection = Connection(LISTENER_PORT)

def get_connection(handler):
    def reqHander(res):
        port = res["port"]
        handler(Connection(port))

    _mainConnection.do_request({}, reqHander)

