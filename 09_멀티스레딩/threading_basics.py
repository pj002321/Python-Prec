# ===== 09. 멀티스레딩 & 비동기 =====
# 목표 연결: ROS2 콜백 구조 이해, 실시간 센서 루프, 병렬 처리

import threading
import asyncio
import time
import queue
import random

# --- Thread: 센서 루프 + 제어 루프 분리 ---
sensor_queue = queue.Queue(maxsize=10)
stop_event = threading.Event()

def sensor_loop():
    """실제 환경: 여기서 LiDAR/카메라 데이터를 읽음."""
    while not stop_event.is_set():
        distance = round(random.uniform(0.3, 3.0), 2)
        sensor_queue.put(distance)
        time.sleep(0.1)

def control_loop():
    """센서 데이터를 받아 속도 명령 계산."""
    while not stop_event.is_set():
        try:
            distance = sensor_queue.get(timeout=0.5)
            speed = 0.0 if distance < 0.5 else min(0.3, distance * 0.1)
            print(f"  거리: {distance:.2f}m → 속도: {speed:.2f}m/s")
        except queue.Empty:
            pass

t_sensor  = threading.Thread(target=sensor_loop,  daemon=True)
t_control = threading.Thread(target=control_loop, daemon=True)

t_sensor.start()
t_control.start()

time.sleep(1.0)   # 1초 실행
stop_event.set()

t_sensor.join(timeout=1)
t_control.join(timeout=1)
print("스레드 종료")

# --- Lock: 공유 상태 보호 ---
robot_state = {"x": 0.0, "y": 0.0}
state_lock = threading.Lock()

def update_position(dx, dy):
    with state_lock:   # 동시 수정 방지
        robot_state["x"] += dx
        robot_state["y"] += dy

# --- asyncio: 비동기 I/O (HTTP 요청, 다중 센서 동시 폴링) ---
async def fetch_sensor(name: str, delay: float):
    await asyncio.sleep(delay)   # 실제: aiohttp 요청
    return {"sensor": name, "value": random.random()}

async def main():
    # 여러 센서를 동시에 폴링
    results = await asyncio.gather(
        fetch_sensor("camera", 0.3),
        fetch_sensor("lidar",  0.1),
        fetch_sensor("imu",    0.05),
    )
    for r in results:
        print(f"  [{r['sensor']}] {r['value']:.3f}")

print("\nasyncio 동시 센서 폴링:")
asyncio.run(main())

# --- 연습 문제 ---
# 1. sensor_loop에서 거리가 0.5m 미만이면 stop_event를 set()해서 자동 정지하게 하세요.
# 2. asyncio를 사용해 3개의 웹 URL에 동시 요청하는 코드를 작성하세요 (aiohttp 사용).
