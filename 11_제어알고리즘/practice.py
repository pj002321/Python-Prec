# ===== 11. 제어알고리즘 — 연습문제 =====

# 문제 1.
# 아래 PIDController 클래스를 완성하세요.
#
# class PIDController:
#     def __init__(self, kp, ki, kd, output_min=-1.0, output_max=1.0):
#         # TODO: 속성 초기화 (integral, prev_error 포함)
#         pass
#
#     def compute(self, setpoint, measured, dt):
#         # TODO: error, integral, derivative 계산 후 출력값 반환
#         # 출력값은 [output_min, output_max] 범위로 제한
#         pass
#
#     def reset(self):
#         # TODO: integral, prev_error 초기화
#         pass


# 문제 2.
# 문제 1의 PIDController로 아래 시나리오를 시뮬레이션하세요.
# - 목표 속도가 매 5스텝마다 0.1 → 0.3 → 0.2 m/s로 순환
# - dt=0.1, 총 30스텝
# - 각 스텝마다 "t=Xs | target=X | speed=X" 형식으로 출력


# 문제 3.
# PIDController에 적분 포화 방지(anti-windup)를 추가하세요.
# integral이 integral_min~integral_max 범위를 벗어나지 않도록 clamp하세요.
# (힌트: compute() 내부에서 self._integral = max(min(...)) 적용)


# 문제 4.
# kp=0.5, ki=0.0, kd=0.0 / kp=3.0, ki=0.0, kd=0.0 두 경우를 비교 출력해서
# P 이득이 클수록 오버슈트가 생기는지 확인하세요.
# 목표: 0.3 m/s, 초기: 0.0, 20스텝
