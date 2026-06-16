# ===== 03. 함수심화 — 연습문제 =====

# 문제 1.
# readings = [0.5, 1.2, 0.8, 2.1, 0.3, 1.9] 에서
# 평균보다 큰 값만 반환하는 함수 above_average(data)를 작성하세요.
# readings = [0.5, 1.2, 0.8, 2.1, 0.3, 1.9]
# def above_average(data):
#     avg = sum(data) / len(data)
#     return [x for x in data if x > avg]

# print(above_average(readings))

# 문제 2.
# 두 좌표 (x1, y1), (x2, y2)의 유클리드 거리를 반환하는 함수를 작성하세요.
# (math.sqrt 사용)
import math
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 문제 3.
# 호출할 때마다 카운트가 1씩 올라가는 클로저 make_counter()를 작성하세요.
# counter = make_counter()
# counter() → 1
# counter() → 2
# counter() → 3

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter=make_counter()
print(counter())
print(counter())
print(counter())

# 문제 4.
# 아래 speeds 리스트를 map()으로 반올림 1자리 float로 변환하고,
# filter()로 0.2 이상인 값만 남기세요.
speeds = [0.123, 0.456, 0.078, 0.312, 0.189]

rounded_speeds = list(map(lambda x: round(x, 1), speeds))
filtered_speeds = list(filter(lambda x: x >= 0.2, rounded_speeds))