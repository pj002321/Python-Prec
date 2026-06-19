# ===== 07. OpenCV 영상처리 — 연습문제 =====
# pip install opencv-python

import cv2
import numpy as np

# 문제 1.
# 640×480 검정 이미지를 만들고
# 왼쪽 절반(0~320)만 크롭해서 "left_half.png"로 저장하세요.
# img = np.zeros((480, 640, 3), dtype=np.uint8)

# left_half = img[:,:320]
# cv2.imwrite("left_half.png", left_half)
# 문제 2.
# 640×480 흰색(255,255,255) 이미지를 만들고
# 그레이스케일로 변환 후 밝기가 200 이상인 픽셀 수를 출력하세요.
img = np.ones((480, 640, 3), dtype=np.uint8) * 255
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
count = np.sum(gray >= 200)
print("밝기 200 이상 픽셀 수:", count)
# 출력결과 : 밝기 200 이상 픽셀 수: 307200


# 문제 3.
# 640×480 검정 이미지에 초록 사각형(100,100)~(300,300)을 그리고
# 사각형 안에 "DETECTED" 텍스트를 추가해서 "detected.png"로 저장하세요.
img = np.zeros((480, 640, 3), dtype=np.uint8)
cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 2)
cv2.putText(img, "DETECTED", (120, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imwrite("detected.png", img)

# 문제 4.
# 랜덤 컬러 이미지를 만들고 Canny 엣지 검출을 적용해 "edges.png"로 저장하세요.
# GaussianBlur (5,5) 먼저 적용할 것.
rnd_img = np.random.randint(0,256,(480,640,3),np.uint8)
blurred = cv2.GaussianBlur(rnd_img, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)
cv2.imwrite("edges.png", edges)