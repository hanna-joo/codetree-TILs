"""
1. 문제
- 턴 1회 = 1번부터 n*n번까지 다음 과정 수행
    - 인접한 8칸 중에 가장 큰 숫자와 가운데 숫자 교환
- return : m번의 턴을 거친 이후 격자판 상태 출력

2. 입력 제한
- 2 <= n <= 20
- 1 <= m <= 100

3. 로직
- 다음 번호 찾기
- 전체 탐색하여 숫자 큰지 비교하고 바꾸기
"""

import sys

def search_pos(target):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == target:
                return i, j


def search_max(cy, cx):
    dy, dx = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    max_val = -sys.maxsize
    max_pos = (0, 0)
    for i in range(8):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0<=ny<n and 0<=nx<n:
            if max_val < grid[ny][nx]:
                max_pos = (ny, nx)
                max_val = grid[ny][nx]
    return max_pos


def change_max(from_pos, to_pos):
    fy, fx = from_pos
    ty, tx = to_pos
    grid[fy][fx], grid[ty][tx] = grid[ty][tx], grid[fy][fx]


def simulate():
    for i in range(1, n*n+1):
        cy, cx = search_pos(i)
        max_pos = search_max(cy, cx)
        change_max((cy, cx), max_pos)


n, m = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]
for _ in range(m):
    simulate()

for i in range(n):
    print(*grid[i])