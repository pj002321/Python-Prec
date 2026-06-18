# ===== 05. 파일과데이터 — 연습문제 =====

# 문제 1.
# 아래 log_data를 "sensor_log.txt"에 저장하되,
# 각 줄이 "0.00s | dist=2.50m | speed=0.30" 형식이 되게 하세요.
#
# log_data = [
#     {"time": 0.0, "distance": 2.5, "speed": 0.30},
#     {"time": 0.1, "distance": 2.2, "speed": 0.30},
#     {"time": 0.2, "distance": 0.8, "speed": 0.10},
#     {"time": 0.3, "distance": 0.4, "speed": 0.00},
# ]

# with open("sensor_log.txt","w") as f:
#     for entry in log_data:
#         f.write(f"{entry['time']:.2f}s | dist={entry['distance']:.2f}m | speed={entry['speed']:.2f}\n")

# 문제 2.
# 문제 1에서 만든 sensor_log.txt를 읽어서
# speed가 0.0인 줄만 출력하세요.

with open("sensor_log.txt","r") as f:
    lines = f.readlines()

result = list(filter(lambda x: "speed=0.00" in x,lines))
for line in result:
    print(line.strip()) 

# 문제 3.
# 아래 config 딕셔너리를 "config.json"으로 저장하고 다시 읽어서
# waypoints의 개수를 출력하세요.
#
import json
import os
config = {
    "robot_id": "TB3-002",
    "max_speed": 0.4,
    "waypoints": [{"x": 0, "y": 0}, {"x": 5, "y": 5}, {"x": 3, "y": 8}]
}

with open("config.json","w") as f:
    json.dump(config,f)

with open("config.json","r") as f:
    loaded = json.load(f)

print(f"waypoints 개수 : {len(loaded['waypoints'])}")
# 문제 4.
# 존재하지 않는 파일 "missing.json"을 열 때
# FileNotFoundError를 잡아서 "파일 없음 — 기본값 사용"을 출력하세요.

try:
    with open("missing.json","r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("파일 없음 — 기본값 사용")
    data = []

os.remove("sensor_log.txt")  
os.remove("config.json")  