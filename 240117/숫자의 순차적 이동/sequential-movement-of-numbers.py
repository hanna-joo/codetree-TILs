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

def in_range(y, x):
    return 0 <= y and y < n and 0 <= x and x < n


def find_pos(num):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                return (i, j)


def find_next_pos(pos):
    dys, dxs = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

    cy, cx = pos

    max_val = -1
    max_pos = (-1, -1)
    for dx, dy in zip(dys, dxs):
        ny, nx = cy + dy, cx + dx
        if in_range(ny, nx) and max_val < grid[ny][nx]:
            max_pos = (ny, nx)
            max_val = grid[ny][nx]
    return max_pos


def swap_pos(pos, next_pos):
    (cy, cx), (ny, nx) = pos, next_pos
    grid[cy][cx], grid[ny][nx] = grid[ny][nx], grid[cy][cx]


def simulate():
    for num in range(1, n*n+1):
        pos = find_pos(num)
        max_pos = find_next_pos(pos)
        swap_pos(pos, max_pos)


n, m = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]

for _ in range(m):
    simulate()

for i in range(n):
    print(*grid[i])