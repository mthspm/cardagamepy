import asyncio
import json
import websockets
import cg_login
import utils

HOST = "25.66.46.176"
PORT = 8765

async def handle_connection(websocket, path, callbacks):
    print(f"Client connected: {websocket.remote_address}")
    try:
        # Handle incoming messages from the client
        async for message in websocket:
            # Parse the message as JSON
            try:
                data = json.loads(message)
            except json.JSONDecodeError:
                # Call the "error" callback function, if provided
                if 'error' in callbacks:
                    await callbacks['error'](websocket, f"Invalid JSON: {message}")
                continue

            # Extract the message type and call the corresponding callback function, if provided
            message_type = data.get('type')
            message_data = data.get('data')
            if message_type in callbacks:
                await callbacks[message_type](websocket, message_data)
            else:
                # Call the "error" callback function, if provided
                if 'error' in callbacks:
                    await callbacks['error'](websocket, f"Invalid message type: {message_type}")
    except websockets.exceptions.ConnectionClosedError as e:
        await handle_on_close(websocket, data)

# Define callback functions for handling incoming messages

async def handle_on_close(websocket, data):
    print(f'client disconnect {data}')
    await websocket.send(json.dumps({'type': 'on_close', 'data': data}))

async def handle_login(websocket, data):
    time = utils.timeNow()
    user = data.get('user')       
    password = data.get('password')

    feedback = cg_login.login(user,password)

    await websocket.send(json.dumps({'type': 'login', 'data': feedback}))

    print(f'[{time}] Attempt login from: {user} {password}')

async def handle_signin(websocket, data):
    time = utils.timeNow()
    user = data.get('user')       
    password = data.get('password')
    passwordconfirm = data.get('passwordconfirm')

    feedback = cg_login.singin(user,password,passwordconfirm)

    await websocket.send(json.dumps({'type': 'signin', 'data': feedback}))

    print(f'[{time}] Attempt signin from: {user} {password}')

async def handle_error(websocket, error_message):
    await websocket.send(json.dumps({'type': 'error', 'message': error_message}))

async def start_server(host, port, callbacks):
# Start the WebSocket server
    async with websockets.serve(lambda websocket, path: handle_connection(websocket, path, callbacks), host, port):
        time = utils.timeNow()

        print(f"[{time}] SERVER STATUS : ONLINE\n"
              f"[{time}] SERVER ADRESS : {host}:{port}\n"
              f"[{time}] CG SERVER VERSION : 0.1\n"
              f"[{time}] GITHUB : https://github.com/Mathlokz/CG-GAME\n")
        await asyncio.Future()  # Run forever

# Define a dictionary of callback functions for different message types
callbacks = {
    'connection': handle_connection,
    'login': handle_login,
    'signin': handle_signin,
    'on_close': handle_on_close
}

# Start the WebSocket server
loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(start_server(HOST, PORT, callbacks))
except KeyboardInterrupt:
    pass
finally:
    tasks = asyncio.all_tasks(loop=loop)
    for task in tasks:
        task.cancel()
    group = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()