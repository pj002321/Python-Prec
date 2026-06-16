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
# def run_server():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server.bind(("127.0.0.1", 9990))
#     server.listen(1)
#     server.settimeout(3.0)
#     # TODO: 연결 수락 → 데이터 수신 → "ACK" 전송
#
# def run_client():
#     time.sleep(0.2)
#     robot_state = {"id": "TB3-001", "battery": 72}
#     # TODO: 서버에 연결 → 데이터 전송 → "ACK" 수신 후 출력


# 문제 2.
# run_client에서 robot_state에 "timestamp": time.time() 필드를 추가하고
# 서버가 수신 시 timestamp를 파싱해서 출력하게 하세요.


# 문제 3.
# 포트 번호를 인자로 받는 simple_server(port) 함수를 만드세요.
# 클라이언트가 연결하면 "HELLO" 를 보내고 연결을 닫습니다.
