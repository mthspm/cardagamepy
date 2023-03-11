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
        ws.send(data)

    #Funcao que trata qualquer data recebida pelo servidor
    #a data recebida passa por 'handler_functions' que filtra
    #pelo type dos dados recebidos o que fazer com o dado
    def on_message(self, ws, message):
        # parse the message as JSON
        data = json.loads(message)

        # get the message type
        message_type = data.get("type")

        # map message types to their corresponding handler functions
        handler_functions = {
            'login': self.handle_login,
            'func2': self.handle_func2,
            'on_open': self.handle_on_open,
        }
        # call the appropriate handler function for the message type
        handler_function = handler_functions.get(message_type)
        if handler_function is not None:
            handler_function(data)
        else:
            print(f"Unhandled event for user '{self.hostname}': {message_type}")


    #Funcoes que tratam os dados recebidos de acordo com seu type.
    def handle_on_open(self, data):
        print(f"Conectado ao servidor com sucessso! -> Feedback do servidor '{self.hostname}': {data}")

    def handle_login(self, data):
        print(f"Received login response for user '{self.hostname}': {data}")

    def handle_func2(self, data):
        print(f"Received func2 message for user '{self.hostname}': {data}")

    def on_error(self, ws, error):
        print(f"WebSocket error for user '{self.hostname}': {error}")

    def on_close(self, ws):
        print(f"WebSocket disconnected for user '{self.hostname}'")