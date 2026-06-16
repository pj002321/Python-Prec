# ===== 03. 함수 심화 =====
# 목표 연결: 센서 처리 유틸, ROS2 콜백 함수, 재사용 가능한 모듈 작성

# --- 기본 함수 + 기본값 인자 ---
def clamp(value, min_val=0.0, max_val=1.0):
    """값을 [min_val, max_val] 범위로 제한."""
    return max(min_val, min(max_val, value))

print(clamp(1.5))          # 1.0
print(clamp(-0.3, -1, 1))  # -0.3

# --- 여러 값 반환 ---
def parse_sensor(raw: str):
    """'x:3.0,y:5.0,theta:1.57' 형식 파싱."""
    parts = dict(item.split(":") for item in raw.split(","))
    return float(parts["x"]), float(parts["y"]), float(parts["theta"])

x, y, theta = parse_sensor("x:3.0,y:5.0,theta:1.57")
print(f"위치: ({x}, {y}), 방향: {theta}rad")

# --- *args, **kwargs ---
def log_event(*tags, level="INFO", **data):
    tag_str = " ".join(f"[{t}]" for t in tags)
    data_str = " ".join(f"{k}={v}" for k, v in data.items())
    print(f"{level} {tag_str} {data_str}")

log_event("SENSOR", "LiDAR", level="WARN", distance=0.3, unit="m")

# --- 람다 & 고차함수 ---
readings = [0.5, 1.2, 0.8, 2.1, 0.3, 1.9]

# 장애물만 필터링
obstacles = list(filter(lambda d: d < 1.0, readings))

# 거리를 cm로 변환
in_cm = list(map(lambda d: round(d * 100), readings))

# 가장 가까운 장애물
nearest = min(readings)

print("장애물:", obstacles)
print("cm 단위:", in_cm)
print("최근접:", nearest)

# --- 클로저: 상태를 가진 함수 ---
def make_moving_average(window_size=5):
    buffer = []
    def update(value):
        buffer.append(value)
        if len(buffer) > window_size:
            buffer.pop(0)
        return sum(buffer) / len(buffer)
    return update

avg = make_moving_average(3)
for r in readings:
    print(f"  입력: {r:.1f} → 이동평균: {avg(r):.3f}")

# --- 연습 문제 ---
# 1. readings에서 평균보다 큰 값만 필터링하는 함수를 작성하세요.
# 2. 두 좌표 (x1,y1), (x2,y2)의 유클리드 거리를 반환하는 함수를 작성하세요.
