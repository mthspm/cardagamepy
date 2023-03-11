import websocket
import json
import asyncio

HOST = "25.66.46.176"
PORT = 8765

def on_open(ws):
    data = json.dumps({'type': 'login', 'username': 'teste', 'password': 'teste'})
    ws.send(data)
    print('login request sended')

def on_message(ws, message):
    # parse the message as JSON
    data = json.loads(message)

    # get the message type
    message_type = data.get("type")

    # map message types to their corresponding handler functions
    handler_functions = {
        'login': handle_login,
        "func2": 'handle_func2',
    }

    # call the appropriate handler function for the message type
    handler_function = handler_functions.get(message_type)
    if handler_function is not None:
        handler_function(data)
    else:
        print("Unhandled event:", message_type)

# define a function to handle the "welcome" message
def handle_login(data):
    print("Received login response:", data)

# define a function to handle the "goodbye" message
def handle_signin(data):
    print("Received goodbye message:", data)

# define a function to handle connection errors
def on_error(ws, error):
    print("WebSocket error:", error)

# define a function to handle disconnection from the server
def on_close(ws, close_status_code, close_msg):
    print("WebSocket disconnected")

ws = websocket.WebSocketApp( 
        f"ws://{HOST}:{PORT}",
        on_open = on_open,
        on_message = on_message,
        on_error = on_error,
        on_close = on_close
    )

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(ws.run_forever())
except KeyboardInterrupt:
    pass
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

