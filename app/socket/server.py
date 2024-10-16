# 서버 코드 (server.py)
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

print("서버가 시작되었습니다.")
#
while True:
    client, addr = server.accept()
    print(f"클라이언트 {addr}가 연결되었습니다.")
    message = client.recv(1024).decode("utf-8")
    print(f"클라이언트로부터 받은 메시지: {message}")
    client.send("메시지를 받았습니다.".encode("utf-8"))
    client.close()
