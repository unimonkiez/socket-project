LISTENER_PORT = 65196

class PortManager:
    def __init__(self):
        self._free_ports = list(range(65201, 65534))
        self._taken_ports = []

    @property
    def available_ports_len(self):
        return len(self._free_ports)

    @property
    def taken_ports_len(self):
        return len(self._taken_ports)
    
    def request_port(self):
        if (self.available_ports_len == 0):
            raise Exception("No ports available, all {} taken".format(self.taken_ports_len))
        
        clientPort = self._free_ports.pop()
        self._taken_ports.append(clientPort)

        def free_port():
            self._free_ports.remove(clientPort)
            self._free_ports.append(clientPort)
        
        return clientPort, free_port
    

