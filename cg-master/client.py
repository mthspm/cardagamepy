import websocket
import json
import socket

class Client:
    #Parametros que inicializam com a classe
    def __init__(self, host="25.66.46.176", port=8765):
        self.hostname = socket.gethostname()
        self.host = host
        self.port = port

    #Funcao connect que de fato conecta o objeto ao server
    def connect(self):
        self.handler_functions = {
            'on_close': self.handle_on_close,
            'error': self.on_error,
            'login': self.handle_login,
            'signin': self.handle_signin,
        }
        self.ws = websocket.WebSocketApp(
            f"ws://{self.host}:{self.port}",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.run_forever()

    #Funcao que executa imediatamente quando o client eh conectado ao servidor
    def on_open(self, ws):
        data = json.dumps({'type': 'on_message', 'username': self.hostname})
        print(f'connected to server {self.host}:{self.port} as {self.hostname}')
        self.ws.send(data)

    def on_close(self, ws, close_status, close_reason):
        data = json.dumps({'type': 'on_close', 'status': close_status, 'reason': close_reason})
        self.ws.send(data)

    def check_connection(self):
        return self.ws.sock and self.ws.sock.connected

    def on_error(self, ws, error):
        print(f"WebSocket error for user '{self.hostname}': {error}")

    def send_data(self, type, data):
        if self.ws.sock and self.ws.sock.connected:
            data = json.dumps({'type': type, 'data': data})
            self.ws.send(data.encode())
        else:
            print("failed on data send attempt : 'no response from server'.")

    def on_message(self, ws, message):
        data = json.loads(message)
        message_type = data.get("type")
        handler_function = self.handler_functions.get(message_type)
        if handler_function is not None:
            handler_function(data)
        else:
            print(f"type not on scope of 'handler_functions' event for user '{self.hostname}': {message_type}")

    #Funcoes que tratam os dados recebidos de acordo com seu type.

    def add_callback(self, type, callback):
        self.handler_functions[type] = callback;

    def remove_call(self, type):
        self.handler_functions.popitem(type)

    def handle_on_close(self, data):
        pass

    def handle_login(self, data):
        print(f"Received login response for user '{self.hostname}': {data}")
        if data.get('data') is True:
            print('login aprovado')
        else:
            print('login reprovado')

    def handle_signin(self, data):
        print(f"Received signin message for user '{self.hostname}': {data}")
        if data.get('data') is True:
            print('registro aprovado')
        else:
            print('registro reprovado')