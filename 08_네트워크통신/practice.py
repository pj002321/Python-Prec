# ===== 08. 네트워크통신 — 연습문제 =====

import socket
import json
import threading
import time

# 문제 1.
# 아래 서버/클라이언트 구조에서
# 서버가 데이터를 받은 뒤 "ACK" 문자열을 클라이언트에게 돌려보내고
# 클라이언트가 그것을 받아서 출력하도록 완성하세요.
#
def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 9990))
    server.listen(1)
    server.settimeout(3.0)
    # TODO: 연결 수락 → 데이터 수신 → "ACK" 전송
    try:
        conn, addr = server.accept()
        print("클라이언트 연결:", addr)
        data = conn.recv(1024)
        print("수신 데이터:", data.decode())
        state = json.loads(data)
        print("Timestamp:", state["timestamp"])
        conn.sendall(b"ACK")
        conn.close()
    except socket.timeout:
        print("서버 타임아웃")
    finally:
        server.close()

def run_client():
    time.sleep(0.2)
    robot_state = {"id": "TB3-001", "battery": 72,"timestamp": time.time()}
    # TODO: 서버에 연결 → 데이터 전송 → "ACK" 수신 후 출력
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9990))
    client.sendall(json.dumps(robot_state).encode())
    ack = client.recv(1024)
    print("ACK 수신:", ack.decode())
    client.close()

def simple_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", port))
    server.listen(1)
    try:
        conn, addr = server.accept()
        print("클라이언트 연결:", addr)
        conn.sendall(b"HELLO")
        conn.close()
    finally:
        server.close()

def simple_client(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", port))
    msg = client.recv(1024).decode()
    print("서버 메시지:", msg)
    client.close()

client_thread = threading.Thread(target=run_client)
server_thread = threading.Thread(target=run_server)
server_thread.start()
client_thread.start()
server_thread.join()
client_thread.join()

# client_thread - send → server_thread - recv → server_thread - send "ACK" → client_thread - recv "ACK" → print
# server_thread - accept → recv → send "ACK"

# 문제 2.
# run_client에서 robot_state에 "timestamp": time.time() 필드를 추가하고
# 서버가 수신 시 timestamp를 파싱해서 출력하게 하세요.



# 문제 3.
# 포트 번호를 인자로 받는 simple_server(port) 함수를 만드세요.
# 클라이언트가 연결하면 "HELLO" 를 보내고 연결을 닫습니다.
