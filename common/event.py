from threading import Thread
from time import sleep
import socket
import json

HOST = '127.0.0.1'

def _listen_handler(s, getIsRunning, handler):
    try:
        while getIsRunning():
            conn, addr = s.accept()
            with conn:
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
    except ConnectionAbortedError:
        pass

def listen(port, handler):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    s.listen()

    isRunning = True
    def getIsRunning():
        nonlocal isRunning
        return isRunning

    def terminateListener():
        nonlocal s
        nonlocal isRunning
        isRunning = False
        s.close()

    thread = Thread(target = _listen_handler, args = (s, getIsRunning, handler, ))
    thread.start()

    return terminateListener

def get_do_request(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, port))

    def do_request(data: dict, handler):
        nonlocal s
        s.sendall(json.dumps(data).encode())
        dataBytes = s.recv(1024)

        if (int.from_bytes(dataBytes, 'big') != 0):
            res = json.loads(dataBytes.decode())
            handler(res)

    return do_request