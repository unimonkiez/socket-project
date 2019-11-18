LISTENER_PORT = 65200

class PortManager:
    def __init__(self):
        self._free_ports = list(range(65201, 65202))
        self._taken_ports = []

    @property
    def available_ports(self):
        return len(self._free_ports)
    
    def request_port(self):
        if (self.available_ports == 0):
            raise Exception("No ports available, all {} taken".format(self.available_ports))
        
        clientPort = self._free_ports.pop()
        self._taken_ports.append(clientPort)

        def free_port():
            self._free_ports.remove(clientPort)
            self._free_ports.append(clientPort)
        
        return clientPort, free_port
    

