import socket

HAMACHI_IPV4 = "25.66.46.176"
HOST = HAMACHI_IPV4
PORT = 7777
IS_CONNECTED = 0

class SocketConnection:
    def __init__(self, ip, port) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
    
    def connect(self):
        try:
            self.socket.connect((HOST, PORT))
            self.connected = True
            print('[Socket] Client connected to the server.')
            return True
        except Exception as e:
            print(f'\n[Socket] Unable to connect to server... \nError {e}\n')
            return False
