from threading import Thread
from time import sleep
import socket
import json

HOST = '127.0.0.1'

def _listen_handler(s, handler):
    try:
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

    def terminateListener():
        nonlocal s
        s.close()

    thread = Thread(target = _listen_handler, args = (s, handler, ))
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