# ===== 09. 멀티스레딩 — 연습문제 =====

import threading
import asyncio
import time
import queue
import random

# 문제 1.
# sensor_loop에서 거리가 0.5m 미만이 감지되면
# stop_event.set()으로 자동 정지하도록 아래 코드를 완성하세요.
#
# sensor_queue = queue.Queue(maxsize=10)
# stop_event = threading.Event()
#
# def sensor_loop():
#     while not stop_event.is_set():
#         distance = round(random.uniform(0.2, 3.0), 2)
#         sensor_queue.put(distance)
#         # TODO: distance < 0.5 이면 stop_event 설정
#         time.sleep(0.1)
#
# def control_loop():
#     while not stop_event.is_set():
#         try:
#             distance = sensor_queue.get(timeout=0.5)
#             print(f"  거리: {distance:.2f}m")
#         except queue.Empty:
#             pass


# 문제 2.
# threading.Lock()을 사용해 두 스레드가 동시에 counter를 증가시킬 때
# 레이스 컨디션 없이 최종값이 정확히 2000이 되도록 하세요.
#
# counter = 0
# # TODO: Lock 추가
#
# def increment():
#     global counter
#     for _ in range(1000):
#         counter += 1   # 이 부분을 안전하게 만드세요
#
# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)


# 문제 3.
# asyncio.gather로 아래 3개 코루틴을 동시에 실행하고 결과를 출력하세요.
# - fetch("camera", 0.3초 지연) → "camera 완료"
# - fetch("lidar",  0.1초 지연) → "lidar 완료"
# - fetch("imu",    0.05초 지연) → "imu 완료"
