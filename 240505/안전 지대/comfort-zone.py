"""
<안전 지대 : DFS>
1. 문제
- 비가 K만큼 온다면 집의 높이가 K 이하인 집들은 모두 물에 잠김
- 안전영역이란 물에 잠기지 않는 집들로 연결된 영역
- 안전 영역의 수가 최대가 되는 K가 여러 개라면 가장 작은 K 출력
- return : 안전 영역의 수를 최대로 만들어주는 K, 안전 영역의 수

2. 입력 및 제한
- 첫 번째 줄 : N, M 공백 (1 <= N, M <= 50)
- 두 번째 줄 : N개의 줄에 걸쳐 각 행에 위치한 M개의 마을 높이 정보 공백 (1 <= 집 높이 <= 100)

3. 로직 : DFS
- K를 1부터 100까지 반복하여 안전지대 탐색
  - 이동 가능 여부(범위내, 높이<K, 방문X) > 방문 > 네 방향 탐색
- 시간복잡도 : O(HNM)
- 공간복잡도 : O(NM)
"""

import sys
sys.setrecursionlimit(10000)

# 입력 변수
N, M = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(N)]

# 글로벌 변수
visited = [[False for _ in range(M)] for _ in range(N)]
K = 0


def initialize_visited():
    for i in range(N):
        for j in range(M):
            visited[i][j] = False


def in_range(y, x):
    return 0 <= y < N and 0 <= x < M


def can_move(y, x):
    if not in_range(y, x):
        return False
    if visited[y][x] or grid[y][x] <= K:
        return False

    return True


def dfs(y, x):
    visited[y][x] = True

    dys, dxs = [-1, 0, 1, 0], [0, -1, 0, 1]

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx

        if can_move(ny, nx):
            dfs(ny, nx)


def get_safezone_num(k):
    global K
    K = k

    initialize_visited()

    safezone_num = 0
    for i in range(N):
        for j in range(M):
            if can_move(i, j):
                dfs(i, j)
                safezone_num += 1
    
    return safezone_num


max_safezone_num = -1
max_safezone_k = 0
max_height = 100

for k in range(1, max_height + 1):
    safezone_num = get_safezone_num(k)
    if safezone_num > max_safezone_num:
        max_safezone_k = k
        max_safezone_num = safezone_num

print(max_safezone_k, max_safezone_num)