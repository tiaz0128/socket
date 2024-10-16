# 클라이언트 코드 (websocket_client.py)
import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "안녕하세요, 웹소켓 서버!"
        await websocket.send(message)
        print(f"서버로 보낸 메시지: {message}")

        response = await websocket.recv()
        print(f"서버로부터 받은 응답: {response}")


asyncio.get_event_loop().run_until_complete(hello())
