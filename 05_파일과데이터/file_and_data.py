# ===== 05. 파일 I/O & 데이터 처리 =====
# 목표 연결: 센서 로그 저장/읽기, 로봇 설정 파일(YAML/JSON), 성능 분석 데이터

import json
import csv
import os

# --- JSON: 로봇 설정 파일 ---
config = {
    "robot_id": "TB3-001",
    "max_speed": 0.5,
    "obstacle_threshold": 0.5,
    "waypoints": [
        {"x": 0.0, "y": 0.0},
        {"x": 3.0, "y": 5.0},
        {"x": 7.0, "y": 2.0}
    ]
}

# 저장
with open("robot_config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

# 읽기
with open("robot_config.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("설정 로드:", loaded["robot_id"])
print("경유지 수:", len(loaded["waypoints"]))

# --- CSV: 센서 로그 기록 ---
log_data = [
    {"time": 0.0, "distance": 2.5, "speed": 0.3},
    {"time": 0.1, "distance": 2.2, "speed": 0.3},
    {"time": 0.2, "distance": 0.8, "speed": 0.1},
    {"time": 0.3, "distance": 0.4, "speed": 0.0},
]

with open("sensor_log.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["time", "distance", "speed"])
    writer.writeheader()
    writer.writerows(log_data)

# CSV 읽기 + 분석
with open("sensor_log.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

distances = [float(r["distance"]) for r in rows]
print(f"\n평균 거리: {sum(distances)/len(distances):.2f}m")
print(f"최소 거리: {min(distances):.2f}m")

# --- 예외처리: 파일이 없을 때 ---
try:
    with open("missing_file.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("\n설정 파일 없음 — 기본값 사용")
    data = {}

# --- 정리 ---
os.remove("robot_config.json")
os.remove("sensor_log.csv")

# --- 연습 문제 ---
# 1. log_data를 텍스트 파일(.txt)로 저장하되, 각 줄이 "0.00s | dist=2.50m | speed=0.30" 형식이 되도록 하세요.
# 2. sensor_log.csv에서 speed가 0.0인 행만 읽어서 출력하세요.
