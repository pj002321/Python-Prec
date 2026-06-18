# ===== 04. OOP — 연습문제 =====

# 문제 1.
# Sensor 클래스를 상속받는 CameraSensor를 만드세요.
# - 추가 속성: resolution (예: "1920x1080"), fps (예: 30)
# - 추가 메서드: capture() → "촬영: 1920x1080 @ 30fps" 출력
#
class Sensor:
    def __init__(self, name, max_range):
        self.name = name
        self.max_range = max_range

class CameraSensor(Sensor):
    def __init__(self, name, max_range, resolution, fps):
        super().__init__(name, max_range)
        self.resolution = resolution
        self.fps = fps

    def capture(self):
        print(f"촬영 : {self.resolution} @ {self.fps}fps")

camera = CameraSensor("Front Camera", 100, "1920x1080", 30)
camera.capture()

# 문제 2.
# RobotNode 클래스를 만드세요.
# - 속성: name, battery (기본값 100)
# - 메서드 check_battery(): battery가 20 이하면 "경고: 배터리 부족" 출력
# - 메서드 publish(topic, data): "[name] → topic: data" 형식 출력

class RobotNode:
    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def check_battery(self):
        if self.battery <= 20:
            print("경고: 배터리 부족")

    def publish(self, topic, data):
        print(f"[{self.name}] → {topic}: {data}")

robot = RobotNode("Alpha", battery=15)
robot.check_battery()
robot.publish("status", "operational")

# 문제 3.
# Vehicle 클래스와 이를 상속하는 Robot 클래스를 만드세요.
# - Vehicle: speed, move(distance) → speed * distance로 소요 시간 계산 후 출력
# - Robot:   name 추가, __repr__ → "Robot(name, speed=...)" 반환

class Vehicle:
    def __init__(self,speed):
        self.speed = speed
    
    def move(self, distance):
        print(f"소요 시간 : {distance/self.speed :.2f} 초")

class Robot(Vehicle):
    def __init__(self, name, speed):
        super().__init__(speed)
        self.name = name

    def __repr__(self):
        return f"Robot({self.name}, speed={self.speed})"
    
robot = Robot("Beta", speed=5)
robot.move(10)
