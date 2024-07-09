import asyncio
import websockets

# Define the WebSocket server
async def handler(websocket, path):
    print(f"[DEBUG] New connection from {websocket.remote_address}")
    async for message in websocket:
        print(f"[DEBUG] Received message: {message}")
        response = f"Echo: {message}"
        await websocket.send(response)
        print(f"[DEBUG] Sent message: {response}")

# Start the WebSocket server
async def main():
    uri = "ws://localhost:8080"
    async with websockets.serve(handler, "localhost", 8080):
        print(f"[DEBUG] WebSocket server started at ws://localhost:8080")
        await asyncio.Future()  # Run forever

# Run the server
if __name__ == "__main__":
    asyncio.run(main())
