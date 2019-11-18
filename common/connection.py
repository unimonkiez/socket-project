from threading import Thread
from time import sleep
import socket
import json

HOST = '127.0.0.1'

def _listen_handler(port, getIsRunning, handler):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, port))
        s.listen()
        while getIsRunning():
            conn, addr = s.accept()
            with conn:
                if (getIsRunning()):
                    print('Connected by', addr)
                    while True:
                        dataBytes = conn.recv(1024)
                        if not dataBytes:
                            break
                        data = json.loads(dataBytes.decode())
                        res: dict = handler(data)
                        if (res != None):
                            conn.send(json.dumps(res).encode())
                        else:
                            conn.send(bytes([0]))
                conn.close()

def listen(port, handler):
    thread = None
    running = True
    def getIsRunning():
        nonlocal running
        return running
    def terminateListener():
        nonlocal running
        running = False

    thread = Thread(target = _listen_handler, args = (port, getIsRunning, handler, ))
    thread.start()

    return terminateListener

def do_request(port, data: dict, handler):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        s.sendall(json.dumps(data).encode())
        dataBytes = s.recv(1024)

        if (int.from_bytes(dataBytes, 'big') != 0):
            res = json.loads(dataBytes.decode())
            handler(res)