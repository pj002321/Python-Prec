# ===== 10. AI기초 — 연습문제 =====
# pip install numpy scikit-learn

import numpy as np

# 문제 1.
# 아래 X, y에 새 데이터 [1.0, 0.2, 70] (레이블=1)을 추가하고
# 정규화 후 KNN으로 분류 결과를 출력하세요.
#
X = np.array([
    [2.5, 0.3, 80],
    [1.8, 0.2, 60],
    [0.6, 0.3, 70],
    [0.4, 0.1, 30],
    [3.0, 0.4, 90],
    [0.3, 0.2, 50],
])
y = np.array([0, 0, 1, 1, 0, 1])

new_data = np.array([1.0,0.2,70])
new_label = np.array([1])

X = np.vstack([X,new_data])
y=np.append(y,new_label)

# 정규화
X_min = X.min(axis=0)
X_max = X.max(axis=0)
X_norm = (X-X_min) / (X_max-X_min)
X_norm = np.round(X_norm,2)
print(f"정규화 데이터 \n {X_norm}")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_norm,y)

query_norm = (np.array([1.0, 0.2, 70]) - X_min) / (X_max - X_min)
print("분류 결과:", knn.predict([query_norm]))

# 문제 2.
# 예측값과 실제값을 비교해서 정확도(accuracy)를 직접 계산하세요.
y_true = np.array([0, 1, 1, 0, 1, 0])
y_pred = np.array([0, 1, 0, 0, 1, 1])
# 정확도 = 맞은 개수 / 전체 개수
correct = (y_true == y_pred)
accuracy = correct.sum()/len(y_true)
print(f"정확도: {accuracy:.2f}")

# 문제 3.
# shape (224, 224, 3) uint8 랜덤 이미지를 만들고
# ImageNet 평균/표준편차로 정규화하세요.
# mean = [0.485, 0.456, 0.406]
# std  = [0.229, 0.224, 0.225]
# 정규화 후 채널별 평균을 출력하세요.
import numpy as np

img = np.random.randint(0,256,(224,224,3), dtype = np.uint8)
def process_image_for_model(image_array, target_size=(224,224)):
    img_float = image_array.astype(np.float32)/255.0
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img_nor = (img_float - mean)/std
    return img_nor

processed = process_image_for_model(img)
print(f"\n 채널별 평균: {processed.mean(axis=(0,1))}")
# 문제 4.
# sklearn KNeighborsClassifier를 사용해
# 문제 1의 데이터로 모델을 학습하고
# [0.5, 0.2, 65] 를 예측하세요.

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_norm,y)

# 예측할 데이터
query = np.array([0.5,0.2,65])
query_norm = (query - X_min)/(X_max-X_min)
print("예측:",knn.predict([query_norm]))