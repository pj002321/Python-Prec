# ===== 04. OOP — 연습문제 =====

# 문제 1.
# Sensor 클래스를 상속받는 CameraSensor를 만드세요.
# - 추가 속성: resolution (예: "1920x1080"), fps (예: 30)
# - 추가 메서드: capture() → "촬영: 1920x1080 @ 30fps" 출력
#
# class Sensor:
#     def __init__(self, name, max_range):
#         self.name = name
#         self.max_range = max_range


# 문제 2.
# RobotNode 클래스를 만드세요.
# - 속성: name, battery (기본값 100)
# - 메서드 check_battery(): battery가 20 이하면 "경고: 배터리 부족" 출력
# - 메서드 publish(topic, data): "[name] → topic: data" 형식 출력


# 문제 3.
# Vehicle 클래스와 이를 상속하는 Robot 클래스를 만드세요.
# - Vehicle: speed, move(distance) → speed * distance로 소요 시간 계산 후 출력
# - Robot:   name 추가, __repr__ → "Robot(name, speed=...)" 반환
