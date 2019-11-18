from common.response import Response, ResponseTypes
from common.port_manager import PortManager, LISTENER_PORT
from common.event import listen
from server.client_manager import ClientManager

class ServerManager:
    def __init__(self):
        self.port_manager = PortManager()
        self._client_managers = []

    def start(self):
        listen(LISTENER_PORT, self._listener_handler)
        print("Server started on port {}\n".format(LISTENER_PORT))

    def _listener_handler(self, data):
        res = None
        try:
            port, freePort = self.port_manager.request_port()

            clientManager = None
            def terminateClient():
                nonlocal clientManager

                freePort()
                self._client_managers.remove(clientManager)

            clientManager = ClientManager(port, terminateClient, data)
            clientManager.start()

            self._client_managers.append(
                terminateClient
            )

            res = Response(ResponseTypes.accept, {
                "port": port,
                "data": clientManager.initialResponse
            })
        except Exception as err:
            res = Response(ResponseTypes.reject, {
                "message": str(err)
            })
        
        return res.toDict()

    
