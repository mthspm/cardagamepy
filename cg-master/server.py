import socket
import threading
from cg_login import connect_data,validate_username,singin,login


HAMACHI_IPV4 = "25.66.46.176"
HOST = HAMACHI_IPV4
PORT = 7777


class Server:

    def __init__(self):
        self.players = []
        self.start()

    def __str__(self) -> str:
        return (f'Server ON:\nOnline Players:\n{self.players}')

    def handle_register(self, data):
        user,password,password_confirm = data

        if singin(user,password,password_confirm):
            return True
        else:
            return False

    def handle_login(self,data):
        user,password = data

        if singin(user,password):
            return True
        else:
            return False

    def handle_data(conn):
        data = conn.recv(1024).decode()
        return data

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            server.bind((HOST, PORT))
            server.listen()
            print('Server is running...')
        except socket.error as e:
            print(str(e))
            return

        while True:
            conn, addr = server.accept()
            print(f'New connection from {addr[0]}:{addr[1]}')

            self.players.append(conn)

Server()