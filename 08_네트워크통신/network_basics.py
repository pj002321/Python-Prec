# ===== 08. 네트워크 & 통신 =====
# 목표 연결: 로봇 모니터링, 네트워크 이해, 멀티로봇 통신, ROS2 DDS 기반 이해

import socket
import json
import threading
import time

# --- TCP 소켓: 로봇 ↔ 서버 통신 기본 패턴 ---

def run_server(host="127.0.0.1", port=9999):
    """모니터링 서버 — 로봇 상태 수신."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(1)
    server.settimeout(3.0)

    try:
        conn, addr = server.accept()
        data = conn.recv(1024).decode()
        state = json.loads(data)
        print(f"[서버] 수신 from {addr}: id={state['id']}, battery={state['battery']}%")
        conn.close()
    except socket.timeout:
        print("[서버] 타임아웃")
    finally:
        server.close()

def run_client(host="127.0.0.1", port=9999):
    """로봇 클라이언트 — 상태 전송."""
    time.sleep(0.2)   # 서버 준비 대기
    robot_state = {"id": "TB3-001", "battery": 72, "speed": 0.3, "x": 3.0, "y": 5.0}

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        client.sendall(json.dumps(robot_state).encode())
        print("[클라이언트] 상태 전송 완료")
    finally:
        client.close()

# 서버와 클라이언트를 각각 스레드에서 실행
t_server = threading.Thread(target=run_server)
t_client = threading.Thread(target=run_client)

t_server.start()
t_client.start()
t_server.join()
t_client.join()

# --- UDP: 빠른 센서 데이터 브로드캐스트 패턴 ---
print("\n--- UDP 패턴 (설명용) ---")
"""
# 송신 (로봇)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(json.dumps(sensor_data).encode(), ("192.168.1.255", 8888))

# 수신 (모니터링 PC)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 8888))
data, addr = sock.recvfrom(1024)
"""

# --- HTTP: REST API로 로봇 명령 (Flask 서버 패턴 미리보기) ---
print("\n--- HTTP REST 패턴 (설명용) ---")
"""
# pip install flask
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/cmd", methods=["POST"])
def receive_command():
    cmd = request.json
    # cmd = {"linear": 0.3, "angular": 0.0}
    return jsonify({"status": "ok"})

# pip install requests
import requests
res = requests.post("http://robot-ip:5000/cmd", json={"linear": 0.3, "angular": 0.0})
"""

# --- 연습 문제 ---
# 1. run_server / run_client를 수정해서 서버가 "ACK" 메시지를 돌려보내도록 하세요.
# 2. 로봇 상태에 "timestamp" 필드를 추가하세요 (time.time() 활용).
