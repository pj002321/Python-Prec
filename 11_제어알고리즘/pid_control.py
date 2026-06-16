# ===== 11. 제어 알고리즘 =====
# 목표 연결: PID 제어, 자율주행 경로 추종, 모터 제어

import time

# --- PID 컨트롤러 클래스 ---
class PIDController:
    def __init__(self, kp: float, ki: float, kd: float,
                 output_min=-1.0, output_max=1.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.output_min = output_min
        self.output_max = output_max

        self._integral = 0.0
        self._prev_error = 0.0

    def compute(self, setpoint: float, measured: float, dt: float) -> float:
        error = setpoint - measured

        self._integral += error * dt
        derivative = (error - self._prev_error) / dt if dt > 0 else 0.0
        self._prev_error = error

        output = (self.kp * error
                + self.ki * self._integral
                + self.kd * derivative)

        return max(self.output_min, min(self.output_max, output))

    def reset(self):
        self._integral = 0.0
        self._prev_error = 0.0

# --- 시뮬레이션: 로봇 속도 제어 ---
print("=== PID 속도 제어 시뮬레이션 ===")
pid = PIDController(kp=1.5, ki=0.1, kd=0.05, output_min=-0.5, output_max=0.5)

target_speed = 0.3      # 목표 속도 (m/s)
current_speed = 0.0
dt = 0.1                # 100ms 주기

for step in range(20):
    control = pid.compute(target_speed, current_speed, dt)
    # 간단한 1차 시스템 모델: 관성 있음
    current_speed += control * dt * 5
    current_speed = max(0.0, min(0.5, current_speed))

    err = target_speed - current_speed
    bar = "█" * int(current_speed / 0.5 * 20)
    print(f"  t={step*dt:.1f}s | speed={current_speed:.3f} | err={err:.3f} | {bar}")

# --- 방향 제어: 목표 각도 추종 ---
print("\n=== PID 방향 제어 시뮬레이션 ===")
heading_pid = PIDController(kp=2.0, ki=0.0, kd=0.3,
                             output_min=-1.0, output_max=1.0)

target_heading = 0.0    # 목표 방향 (rad)
current_heading = 1.57  # 현재 90도

for step in range(15):
    angular_vel = heading_pid.compute(target_heading, current_heading, dt)
    current_heading += angular_vel * dt
    print(f"  heading={current_heading:.3f}rad | cmd={angular_vel:.3f}rad/s")

# --- 연습 문제 ---
# 1. kp, ki, kd 값을 바꿔서 오버슈트(목표 초과), 진동, 느린 수렴을 관찰하세요.
# 2. 목표 속도가 1초마다 0.1 → 0.3 → 0.2 m/s로 바뀌는 시나리오를 구현하세요.
# 3. PIDController에 적분 포화 방지 (anti-windup) 기능을 추가하세요.
