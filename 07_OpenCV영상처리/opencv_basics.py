# ===== 07. OpenCV 영상처리 =====
# 목표 연결: AI 영상기법, 사물인식 전처리, 카메라 입력 처리
# 설치: pip install opencv-python

import cv2
import numpy as np

# --- 이미지 생성 (카메라 없이 테스트용) ---
# 실제 카메라: cap = cv2.VideoCapture(0)
img = np.zeros((480, 640, 3), dtype=np.uint8)  # 검정 배경

# 도형 그리기 (로봇 시뮬레이션 시각화 패턴)
cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 2)   # 초록 사각형
cv2.circle(img, (400, 200), 50, (0, 0, 255), -1)              # 빨간 원 (채움)
cv2.line(img, (0, 240), (640, 240), (255, 255, 0), 1)         # 수평선
cv2.putText(img, "Robot View", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imwrite("output.png", img)
print("output.png 저장 완료")

# --- 색상 공간 변환 ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print("그레이 shape:", gray.shape)   # (480, 640) — 채널 없음

# --- 엣지 검출 (장애물/차선 감지 기반) ---
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
cv2.imwrite("edges.png", edges)
print("edges.png 저장 완료")

# --- 색상 마스킹 (특정 색 객체 추적) ---
# 빨간 원 마스킹
lower_red = np.array([0, 0, 200])    # BGR
upper_red = np.array([50, 50, 255])
mask = cv2.inRange(img, lower_red, upper_red)
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite("red_mask.png", result)
print("red_mask.png 저장 완료")

# --- 리사이즈 (AI 모델 입력 크기 맞추기) ---
resized = cv2.resize(img, (224, 224))    # MobileNet 입력 크기
print("리사이즈:", resized.shape)

# --- 카메라 루프 패턴 (실제 사용 시) ---
"""
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Camera", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
"""

# --- 연습 문제 ---
# 1. output.png를 읽어서 왼쪽 절반만 크롭한 이미지를 저장하세요.
# 2. 그레이스케일 이미지에서 밝기가 200 이상인 픽셀 수를 세세요.
# 3. 이미지에 초록 사각형 안에 "DETECTED" 텍스트를 추가하세요.
