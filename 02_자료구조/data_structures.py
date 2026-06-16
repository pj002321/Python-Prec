# ===== 02. 자료구조 =====
# 목표 연결: 센서 데이터 버퍼, ROS2 메시지 파싱, 경로 좌표 관리

# --- 리스트: 시계열 센서 데이터 ---
lidar_distances = [1.2, 0.8, 2.5, 0.3, 1.9]

lidar_distances.append(1.1)       # 새 데이터 추가
lidar_distances.pop(0)             # 오래된 데이터 제거 (슬라이딩 윈도우)
print("LiDAR:", lidar_distances)

# 리스트 컴프리헨션 — 장애물 필터링
obstacles = [d for d in lidar_distances if d < 1.0]
print("장애물 감지 거리:", obstacles)

# --- 튜플: 변하지 않는 좌표 ---
waypoint_1 = (3.0, 5.0)    # (x, y)
waypoint_2 = (7.0, 2.0)
path = [waypoint_1, waypoint_2, (10.0, 10.0)]

for i, (x, y) in enumerate(path):
    print(f"  경유지 {i}: x={x}, y={y}")

# --- 딕셔너리: 로봇 상태 구조체 ---
robot_state = {
    "id": "TB3-001",
    "position": {"x": 3.0, "y": 5.0, "theta": 1.57},
    "velocity": 0.5,
    "battery": 78,
    "sensors": ["camera", "lidar", "imu"]
}

print("현재 위치:", robot_state["position"])
print("센서 목록:", robot_state["sensors"])

# 딕셔너리 업데이트
robot_state["battery"] = 75
robot_state["position"]["x"] += 0.1

# --- 셋: 중복 없는 감지 객체 ---
detected_objects = {"사람", "의자", "사람", "책상", "의자"}
print("감지된 객체 (중복 제거):", detected_objects)

# --- 연습 문제 ---
# 1. lidar_distances에서 평균값을 구하세요 (sum, len 활용).
# 2. robot_state에 "mode": "자율주행" 키를 추가하세요.
# 3. path에서 x좌표만 추출한 리스트를 만드세요.
