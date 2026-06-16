# ===== 01. 기본 문법 =====
# 목표 연결: 모든 카테고리의 기반 / ROS2 노드 작성 기초

# --- 변수와 타입 ---
speed = 1.5          # float: 로봇 속도 (m/s)
sensor_name = "LiDAR"
is_active = True
battery = 85         # int: 배터리 %

print(type(speed), type(sensor_name), type(is_active))

# --- 타입 변환 ---
raw_input = "3.14"
value = float(raw_input)   # 센서에서 문자열로 들어온 값을 숫자로
print(value * 2)

# --- 문자열 포매팅 (f-string) ---
robot_id = "TB3-001"
status = f"[{robot_id}] 배터리: {battery}% | 속도: {speed}m/s"
print(status)

# --- 조건문 ---
if battery < 20:
    print("배터리 부족 — 복귀")
elif battery < 50:
    print("배터리 주의")
else:
    print("정상 운행")

# --- 반복문 ---
sensor_readings = [0.5, 1.2, 0.8, 2.1, 0.3]
for i, val in enumerate(sensor_readings):
    print(f"  센서[{i}]: {val}m")

# while — 제어 루프 패턴 (ROS2 spin과 유사)
count = 0
while count < 3:
    print(f"  루프 {count}")
    count += 1

# --- 연습 문제 ---
# 1. 속도가 0.0~2.0 사이일 때만 "유효한 속도", 아니면 "범위 초과"를 출력하세요.
# 2. sensor_readings 중 1.0 이상인 값만 출력하세요.
