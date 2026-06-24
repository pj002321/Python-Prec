# ===== 13. 경로 계획 — A* 알고리즘 =====
# 목표 연결: 자율주행 경로 탐색, 장애물 회피, 그리드 맵 탐색

import heapq
import numpy as np

# --- A* 핵심 개념 ---
# f(n) = g(n) + h(n)
#   g(n) : 시작점 → 현재 노드까지 실제 비용
#   h(n) : 현재 노드 → 목표까지 추정 비용 (휴리스틱)
#   f(n) : 총 예상 비용 → 이 값이 작은 노드를 먼저 탐색
#
# 휴리스틱 h(n) 종류:
#   맨해튼 거리 : |dx| + |dy|         → 4방향 이동
#   유클리드 거리: sqrt(dx²+dy²)       → 8방향 이동
#   체비쇼프 거리: max(|dx|, |dy|)     → 8방향 동일 비용


# --- 그리드 맵 정의 ---
# 0 = 이동 가능, 1 = 장애물
GRID = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
])

START = (0, 0)
GOAL  = (6, 6)

# 4방향 이동 (상하좌우)
DIRECTIONS_4 = [(-1,0),(1,0),(0,-1),(0,1)]

# 8방향 이동 (대각선 포함)
DIRECTIONS_8 = [(-1,0),(1,0),(0,-1),(0,1),
                (-1,-1),(-1,1),(1,-1),(1,1)]


def heuristic_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristic_euclidean(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5


def astar(grid, start, goal, directions=DIRECTIONS_4, heuristic=heuristic_manhattan):
    rows, cols = grid.shape
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # 경로 역추적
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)
            r, c = neighbor

            if not (0 <= r < rows and 0 <= c < cols):
                continue
            if grid[r][c] == 1:
                continue

            # 대각선 이동 비용은 √2
            move_cost = 1.414 if dr != 0 and dc != 0 else 1.0
            tentative_g = g_score[current] + move_cost

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor))

    return None   # 경로 없음


def print_grid(grid, path=None, start=None, goal=None):
    symbols = {0: '.', 1: '█'}
    display = [[symbols[v] for v in row] for row in grid.tolist()]

    if path:
        for r, c in path:
            display[r][c] = '*'
    if start:
        display[start[0]][start[1]] = 'S'
    if goal:
        display[goal[0]][goal[1]] = 'G'

    for row in display:
        print('  ' + ' '.join(row))


# --- 실행: 4방향 A* ---
print("=== A* 경로 탐색 (4방향, 맨해튼) ===")
path4 = astar(GRID, START, GOAL, DIRECTIONS_4, heuristic_manhattan)
print(f"경로 길이: {len(path4)}칸")
print_grid(GRID, path4, START, GOAL)

# --- 실행: 8방향 A* ---
print("\n=== A* 경로 탐색 (8방향, 유클리드) ===")
path8 = astar(GRID, START, GOAL, DIRECTIONS_8, heuristic_euclidean)
print(f"경로 길이: {len(path8)}칸")
print_grid(GRID, path8, START, GOAL)


# --- 비교: BFS (휴리스틱 없음) vs A* ---
from collections import deque

def bfs(grid, start, goal):
    rows, cols = grid.shape
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == goal:
            return path
        for dr, dc in DIRECTIONS_4:
            r, c = current[0]+dr, current[1]+dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and (r,c) not in visited:
                visited.add((r,c))
                queue.append(path + [(r,c)])
    return None

print("\n=== BFS vs A* 비교 ===")
path_bfs = bfs(GRID, START, GOAL)
print(f"BFS 경로 길이  : {len(path_bfs)}칸")
print(f"A*(4방향) 길이 : {len(path4)}칸")
print(f"A*(8방향) 길이 : {len(path8)}칸")
print("→ A*는 휴리스틱으로 불필요한 탐색을 줄여 더 빠르게 최단경로 탐색")


# --- 연습 문제 ---
# 1. GRID에 장애물을 추가해서 경로가 바뀌는지 확인하세요.
#
# 2. START = (0,0), GOAL = (6,0) 처럼 목표를 바꿔보고
#    경로가 올바르게 탐색되는지 확인하세요.
#
# 3. 장애물로 목표에 도달 불가능한 맵을 만들고
#    astar()가 None을 반환하는지 확인하세요.
