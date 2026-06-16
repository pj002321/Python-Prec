# ===== 06. NumPy 수치계산 =====
# 목표 연결: 센서 데이터 배열 처리, 좌표 변환, AI 모델 입력 전처리, PID 계산
# 설치: pip install numpy

import numpy as np

# --- 배열 기초 ---
# 라이다 360도 스캔 데이터 (360개 거리값)
scan = np.array([2.5, 1.2, 0.8, 3.1, 0.4, 1.9, 2.2, 0.6])

print("평균:", scan.mean())
print("최솟값:", scan.min(), "/ 인덱스:", scan.argmin())
print("1m 미만:", scan[scan < 1.0])          # 불리언 인덱싱

# --- 좌표 변환 (2D 회전행렬) ---
# 로봇 기준 좌표를 월드 좌표로 변환
def rotate_2d(points, theta):
    """points: (N,2) 배열, theta: 회전각(rad)"""
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    return points @ R.T

robot_points = np.array([[1.0, 0.0], [2.0, 0.5], [0.5, -0.3]])
theta = np.pi / 4   # 45도
world_points = rotate_2d(robot_points, theta)
print("\n로봇 좌표:\n", robot_points)
print("월드 좌표:\n", np.round(world_points, 3))

# --- 이미지 데이터 전처리 패턴 ---
# 카메라 이미지는 (H, W, C) shape의 numpy 배열
fake_image = np.random.randint(0, 256, size=(480, 640, 3), dtype=np.uint8)
print("\n이미지 shape:", fake_image.shape)

# 정규화 (0~1 범위로) — AI 모델 입력 전처리
normalized = fake_image.astype(np.float32) / 255.0
print("정규화 후 최대:", normalized.max())

# 크롭 — 관심 영역(ROI) 추출
roi = fake_image[100:300, 200:400, :]
print("ROI shape:", roi.shape)

# --- 통계: 성능 분석 ---
path_errors = np.array([0.02, 0.05, 0.03, 0.08, 0.01, 0.06, 0.04])
print(f"\n경로 오차 RMSE: {np.sqrt(np.mean(path_errors**2)):.4f}m")
print(f"표준편차: {path_errors.std():.4f}m")

# --- 연습 문제 ---
# 1. scan 배열에서 1m~2m 사이 값만 추출하세요 (불리언 인덱싱).
# 2. 1~10까지 균등 간격으로 20개의 값을 만드세요 (np.linspace).
# 3. (3,3) 단위행렬을 만들고 역행렬을 구하세요 (np.eye, np.linalg.inv).
