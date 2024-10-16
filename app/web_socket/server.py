# 서버 코드 (websocket_server.py)
import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        print(f"클라이언트로부터 받은 메시지: {message}")
        await websocket.send(f"에코: {message}")


start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
