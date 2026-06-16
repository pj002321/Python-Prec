# ===== 02. 자료구조 — 연습문제 =====

# 문제 1.
# lidar_distances = [1.2, 0.8, 2.5, 0.3, 1.9] 의 평균값을 구하세요.
# (sum(), len() 만 사용)

# lidar_distances = [1.2, 0.8, 2.5, 0.3, 1.9] 
# s = sum(lidar_distances)/len(lidar_distances)
# print(s)

# 문제 2.
# robot_state = {"id": "TB3-001", "battery": 78} 에
# "mode": "자율주행" 키를 추가하고 전체 딕셔너리를 출력하세요.
# obot_state = {"id": "TB3-001", "battery": 78,"mode": "자율주행"}

# print(f"{obot_state['id']}")
# print(f"{obot_state['battery']}")
# print(f"{obot_state['mode']}")
# 문제 3.
# path = [(3.0, 5.0),  (7.0, 2.0), (10.0, 10.0)] 에서
# x좌표만 추출한 리스트를 리스트 컴프리헨션으로 만드세요.
# path = [(3.0, 5.0),  (7.0, 2.0), (10.0, 10.0)]
# print([x for x,y in path])


# 문제 4.
# 아래 detected 리스트에서 중복을 제거하고 정렬해서 출력하세요.
 # detected = ["사람", "의자", "사람", "책상", "의자", "책상", "로봇"]
detected = {"사람", "의자", "사람", "책상", "의자", "책상", "로봇"}
print(sorted(detected))