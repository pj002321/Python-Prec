# ===== 12. 센서 퓨전 & 칼만 필터 =====
# 목표 연결: 노이즈 있는 센서 데이터 정제, 위치 추정, IMU 퓨전

import numpy as np

# --- 칼만 필터 개념 ---
# 실제 센서는 항상 노이즈를 포함한다.
# 칼만 필터는 "예측"과 "측정"을 반복하며 실제값을 추정한다.
#
# 두 단계:
#   1. Predict: 이전 상태로 현재 상태 예측
#   2. Update : 실제 센서값으로 예측을 보정
#
# 핵심 변수:
#   x  : 상태 추정값 (예: 위치)
#   P  : 추정 불확실성 (공분산)
#   Q  : 프로세스 노이즈 (모델 오차)
#   R  : 측정 노이즈 (센서 오차)
#   K  : 칼만 게인 (예측 vs 측정 신뢰 비율)


# --- 1D 칼만 필터 클래스 ---
class KalmanFilter1D:
    def __init__(self, process_noise=1.0, measurement_noise=10.0):
        self.x = 0.0   # 상태 추정값
        self.P = 1.0   # 추정 불확실성
        self.Q = process_noise       # 프로세스 노이즈
        self.R = measurement_noise   # 측정 노이즈

    def predict(self):
        # 상태는 변하지 않는다고 가정 (등속 없음), 불확실성만 증가
        self.P += self.Q

    def update(self, measurement: float):
        # 칼만 게인: P가 크면(불확실) 측정값을 더 신뢰
        K = self.P / (self.P + self.R)
        self.x += K * (measurement - self.x)
        self.P *= (1 - K)
        return self.x


# --- 시뮬레이션: 노이즈 있는 거리 센서 정제 ---
print("=== 1D 칼만 필터: 거리 센서 노이즈 제거 ===")

np.random.seed(42)
true_position = 5.0          # 실제 위치 (고정)
noise_std = 2.0              # 센서 노이즈 표준편차

kf = KalmanFilter1D(process_noise=0.1, measurement_noise=noise_std**2)

print(f"{'step':>4} | {'측정값':>8} | {'추정값':>8} | {'실제값':>8}")
print("-" * 40)

for step in range(15):
    raw = true_position + np.random.normal(0, noise_std)   # 노이즈 측정값
    kf.predict()
    estimated = kf.update(raw)
    print(f"  {step:>2}  | {raw:>8.3f} | {estimated:>8.3f} | {true_position:>8.3f}")


# --- 시뮬레이션: 움직이는 로봇 위치 추정 ---
print("\n=== 이동 로봇 위치 추정 ===")
# 로봇이 매 스텝 0.5m씩 이동, GPS는 노이즈 포함

class KalmanFilter1D_Moving:
    def __init__(self, process_noise=0.5, measurement_noise=4.0):
        self.x = 0.0
        self.P = 1.0
        self.Q = process_noise
        self.R = measurement_noise

    def predict(self, velocity: float, dt: float):
        self.x += velocity * dt    # 예측: 속도로 위치 갱신
        self.P += self.Q

    def update(self, measurement: float):
        K = self.P / (self.P + self.R)
        self.x += K * (measurement - self.x)
        self.P *= (1 - K)
        return self.x

kf2 = KalmanFilter1D_Moving()
velocity = 0.5   # m/s
dt = 1.0         # 1초 주기
gps_noise = 2.0

print(f"{'step':>4} | {'GPS(노이즈)':>12} | {'칼만추정':>10} | {'실제위치':>10}")
print("-" * 46)

real_pos = 0.0
for step in range(10):
    real_pos += velocity * dt
    gps = real_pos + np.random.normal(0, gps_noise)

    kf2.predict(velocity, dt)
    estimated = kf2.update(gps)

    print(f"  {step:>2}  | {gps:>12.3f} | {estimated:>10.3f} | {real_pos:>10.3f}")


# --- 센서 퓨전 개념: GPS + IMU ---
print("\n=== 센서 퓨전 개념 (GPS + IMU) ===")
# GPS: 절대 위치, 느리고 노이즈 큼
# IMU: 가속도 적분으로 위치 추정, 빠르지만 누적 오차 있음
# → 칼만 필터로 두 센서를 융합해 정확도 향상

gps_noise_std = 3.0
imu_noise_std = 0.3

real_positions = [i * 0.5 for i in range(10)]
gps_readings = [p + np.random.normal(0, gps_noise_std) for p in real_positions]
imu_readings = [p + np.random.normal(0, imu_noise_std) for p in real_positions]

# 단순 가중 평균 퓨전 (칼만 게인 역할)
w_gps = (1 / gps_noise_std**2)
w_imu = (1 / imu_noise_std**2)

print(f"{'step':>4} | {'GPS':>8} | {'IMU':>8} | {'퓨전결과':>10} | {'실제':>6}")
print("-" * 48)
for i in range(10):
    fused = (w_gps * gps_readings[i] + w_imu * imu_readings[i]) / (w_gps + w_imu)
    print(f"  {i:>2}  | {gps_readings[i]:>8.3f} | {imu_readings[i]:>8.3f} | {fused:>10.3f} | {real_positions[i]:>6.2f}")


# --- 연습 문제 ---
# 1. KalmanFilter1D의 measurement_noise(R)를 1, 10, 100으로 바꿔서
#    추정값이 어떻게 달라지는지 관찰하세요. (R이 크면 측정을 덜 신뢰)
#
# 2. 이동 로봇 시뮬레이션에서 velocity를 매 스텝 변화시켜보세요.
#    (예: step 5부터 velocity = 1.0)
#
# 3. GPS + IMU 퓨전에서 w_gps, w_imu 가중치를 직접 조정해보고
#    노이즈가 큰 센서의 가중치를 낮추면 결과가 어떻게 개선되는지 확인하세요.
