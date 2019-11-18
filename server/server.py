from common.response import Response, ResponseTypes
from common.port_manager import PortManager, LISTENER_PORT
from common.event import listen

class Server:
    def __init__(self):
        self.port_manager = PortManager()

    def start(self):
        listen(LISTENER_PORT, self._listener_handler)

    def _listener_handler(self):
        res = None
        try:
            port = self.port_manager.request_port()
            res = Response(ResponseTypes.accept, {
                "port": port
            })
        except Exception as err:
            res = Response(ResponseTypes.reject, {
                "message": str(err)
            })
        
        return res.toDict()

    
