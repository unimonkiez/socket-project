LISTENER_PORT = 65260

class PortManager:
    def __init__(self):
        self._free_ports = list(range(65261, 65263))
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
            nonlocal clientPort

            self._taken_ports.remove(clientPort)
            self._free_ports.append(clientPort)
        
        return clientPort, free_port
    

