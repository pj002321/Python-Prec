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


# 문제 2.
# 문제 1에서 만든 sensor_log.txt를 읽어서
# speed가 0.0인 줄만 출력하세요.


# 문제 3.
# 아래 config 딕셔너리를 "config.json"으로 저장하고 다시 읽어서
# waypoints의 개수를 출력하세요.
#
# config = {
#     "robot_id": "TB3-002",
#     "max_speed": 0.4,
#     "waypoints": [{"x": 0, "y": 0}, {"x": 5, "y": 5}, {"x": 3, "y": 8}]
# }


# 문제 4.
# 존재하지 않는 파일 "missing.json"을 열 때
# FileNotFoundError를 잡아서 "파일 없음 — 기본값 사용"을 출력하세요.
