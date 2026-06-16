# ===== 10. 인공지능 기초 =====
# 목표 연결: 인공지능 기초, 사물인식 딥러닝, 경량 모델, 온디바이스 AI
# 설치: pip install numpy scikit-learn

import numpy as np

# --- 머신러닝 핵심 개념: 직접 구현 ---

# 1. 데이터: 센서값으로 "안전/위험" 분류
# features: [거리(m), 속도(m/s), 배터리(%)]
X = np.array([
    [2.5, 0.3, 80],   # 안전
    [1.8, 0.2, 60],   # 안전
    [0.6, 0.3, 70],   # 위험
    [0.4, 0.1, 30],   # 위험
    [3.0, 0.4, 90],   # 안전
    [0.3, 0.2, 50],   # 위험
])
y = np.array([0, 0, 1, 1, 0, 1])   # 0=안전, 1=위험

# 2. 정규화 (0~1 범위로) — 모델 학습 안정성
X_min = X.min(axis=0)
X_max = X.max(axis=0)
X_norm = (X - X_min) / (X_max - X_min)
print("정규화된 데이터:\n", np.round(X_norm, 2))

# 3. 간단한 거리 기반 분류기 (KNN 개념)
def predict_knn(X_train, y_train, x_query, k=3):
    distances = np.linalg.norm(X_train - x_query, axis=1)
    nearest_idx = np.argsort(distances)[:k]
    votes = y_train[nearest_idx]
    return int(votes.sum() > k / 2)

new_robot = np.array([0.5, 0.2, 65])
new_norm = (new_robot - X_min) / (X_max - X_min)
pred = predict_knn(X_norm, y, new_norm)
print(f"\n새 상황 {new_robot} → {'위험' if pred else '안전'}")

# --- scikit-learn으로 동일 작업 ---
try:
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import cross_val_score

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_norm, y)

    scores = cross_val_score(knn, X_norm, y, cv=3)
    print(f"\nsklearn KNN 정확도: {scores.mean():.2f}")
    print("예측:", knn.predict([new_norm]))

except ImportError:
    print("sklearn 미설치: pip install scikit-learn")

# --- 딥러닝 모델 입력 전처리 패턴 ---
def preprocess_image_for_model(image_array, target_size=(224, 224)):
    """YOLO/MobileNet 계열 전처리."""
    # 1. 리사이즈 (OpenCV 없이 numpy만으로 개념 설명)
    # 실제: img = cv2.resize(image_array, target_size)
    # 2. 정규화
    img_float = image_array.astype(np.float32) / 255.0
    # 3. 평균 빼기 (ImageNet 통계)
    mean = np.array([0.485, 0.456, 0.406])
    std  = np.array([0.229, 0.224, 0.225])
    img_normalized = (img_float - mean) / std
    # 4. (H,W,C) → (1,C,H,W) — 배치 + 채널 우선 (PyTorch)
    # img_tensor = img_normalized.transpose(2,0,1)[np.newaxis, :]
    return img_normalized

fake_img = np.random.randint(0, 256, (224, 224, 3), dtype=np.uint8)
processed = preprocess_image_for_model(fake_img)
print(f"\n전처리 후 평균: {processed.mean():.3f}, 표준편차: {processed.std():.3f}")

# --- 연습 문제 ---
# 1. X에 새 데이터 [1.0, 0.2, 70]을 추가하고 레이블을 붙여 다시 분류하세요.
# 2. 정확도(accuracy)를 직접 계산하세요: 예측값 vs 실제값 비교.
