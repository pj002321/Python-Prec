# ===== 04. 객체지향 프로그래밍 (OOP) =====
# 목표 연결: ROS2 노드 클래스 구조, 로봇/센서 모델링, AI Agent 설계

import math

# --- 기본 클래스 ---
class Sensor:
    def __init__(self, name: str, max_range: float):
        self.name = name
        self.max_range = max_range
        self._reading = 0.0         # _ : 내부 변수 관례

    def update(self, value: float):
        self._reading = max(0.0, min(value, self.max_range))

    def get(self) -> float:
        return self._reading

    def is_obstacle(self, threshold=1.0) -> bool:
        return self._reading < threshold

    def __repr__(self):
        return f"Sensor({self.name}, {self._reading:.2f}m)"

lidar = Sensor("LiDAR", max_range=10.0)
lidar.update(0.7)
print(lidar)
print("장애물?", lidar.is_obstacle())

# --- 상속 ---
class UltrasonicSensor(Sensor):
    def __init__(self, name: str, angle_deg: float):
        super().__init__(name, max_range=4.0)   # 초음파는 최대 4m
        self.angle_deg = angle_deg

    def get_vector(self):
        angle_rad = math.radians(self.angle_deg)
        return self._reading * math.cos(angle_rad), self._reading * math.sin(angle_rad)

us = UltrasonicSensor("US_FRONT", angle_deg=0)
us.update(1.5)
print(us.get_vector())

# --- ROS2 노드 구조 미리보기 (실제 ROS2 없이 패턴만) ---
class RobotNode:
    def __init__(self, node_name: str):
        self.name = node_name
        self.velocity = 0.0
        self.position = {"x": 0.0, "y": 0.0, "theta": 0.0}
        self._subscribers = {}
        self._publishers = {}

    def subscribe(self, topic: str, callback):
        self._subscribers[topic] = callback
        print(f"[{self.name}] 구독: {topic}")

    def publish(self, topic: str, data: dict):
        print(f"[{self.name}] 발행 → {topic}: {data}")

    def on_sensor_data(self, msg: dict):
        """센서 콜백 — ROS2에서 @subscriber 처럼 동작."""
        dist = msg.get("distance", 999)
        if dist < 0.5:
            self.velocity = 0.0
            self.publish("/cmd_vel", {"linear": 0.0, "angular": 0.0})
            print("  긴급 정지!")
        else:
            self.velocity = 0.3
            self.publish("/cmd_vel", {"linear": 0.3, "angular": 0.0})

node = RobotNode("navigation_node")
node.subscribe("/scan", node.on_sensor_data)
node.on_sensor_data({"distance": 0.3})
node.on_sensor_data({"distance": 2.0})

# --- 연습 문제 ---
# 1. CameraSensor 클래스를 Sensor로부터 상속받아 만드세요.
#    - 추가 속성: resolution (e.g. "1920x1080"), fps
#    - 추가 메서드: capture() → "촬영: {resolution}@{fps}fps" 출력
# 2. RobotNode에 배터리 레벨 속성을 추가하고, 20% 이하면 publish로 경고를 보내세요.
