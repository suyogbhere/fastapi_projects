from fastapi import FastAPI, WebSocket,WebSocketDisconnect, Query, Depends, Cookie , WebSocketException, status
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()


html = """
<!DOCTYPE  html>
<html>
    <head>
        <title>Chat Application</title>
    </head>
    <body>
        <h1>  Websocket Chat </h1>
        <h2>Your ID: <span id="ws-id"></span></h2>

        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off" />
            <button> Send </button>
        </form>
        <ul id="messages">

        </ul>

        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id ;
            var ws = new WebSocket(`ws://localhost:8000/ws/${client_id}`);
            ws.onmessage = function(event){
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };

            function sendMessage(event) {
            var input = document.getElementById("messageText")
            ws.send(input.value)
            input.value =''
            event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)


    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)


    async def send_personal_message(self, message: str, websocket: WebSocket):
        try:
            await websocket.send_text(message)
        except(WebSocketDisconnect, RuntimeError):
            pass

    async def broadcast(self, message:str):
        try:
            for connection in self.active_connections:
                await connection.send_text(message)
        except(WebSocketDisconnect, RuntimeError):
            await self.disconnect(connection)

manager = ConnectionManager()



@app.get("/")
async def home():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says : {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"client #{client_id} left the chat")
        print("Client Disconnect")