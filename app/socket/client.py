# 클라이언트 코드 (client.py)
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

client.send("안녕하세요, 서버!".encode("utf-8"))
response = client.recv(1024).decode("utf-8")
print(f"서버로부터 받은 응답: {response}")

client.close()
