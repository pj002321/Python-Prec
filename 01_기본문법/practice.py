# ===== 01. 기본문법 — 연습문제 =====

# 문제 1.
# speed 변수에 1.5를 저장하고,
# 0.0~2.0 범위 안이면 "유효한 속도", 아니면 "범위 초과"를 출력하세요.
speed = 2.5

# if 0.0 <= speed <= 2.0:
#     print("유효한 속도")
# else:
#     print("범위 초과")

# 문제 2.
# sensor_readings = [0.5, 1.2, 0.8, 2.1, 0.3] 

# # 1.0 이상인 값만 for문으로 출력하세요.
# for i, val in sensor_readings:
#     if val >= 1.0 :
#         print(val)


# 문제 3.
# robot_id = "TB3-001", battery = 85 를 이용해
# "[TB3-001] 배터리: 85%" 형식으로 f-string 출력하세요.
# robot_id = "TB3-001"
# battery = 85

# print(f"[TB3-001] 배터리: {battery}%")

# 문제 4.
# 1부터 10까지 숫자 중 짝수만 출력하는 while문을 작성하세요.
i=2
while(i<=10) :
    print(f"{i}")
    i+=2
 