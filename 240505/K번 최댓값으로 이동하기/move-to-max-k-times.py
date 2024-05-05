"""
<K번 최댓값으로 이동하기 : BFS>
1. 문제
- 1번 이동 = A점에서 B점으로 이동
    - A칸 값인 P보다 작은 칸으로만 이동해서 갈 수 있어야 함
    - B점 우선순위 : 가장 큰 값 -> 가장 작은 행 -> 가장 작은 열
- 단, k번 반복하지 못했지만 새로 이동할 위치가 없다면 종료
- return : k번 특정 움직임을 반복한 후 위치 (r, c)

2. 입력 및 제한
- 첫 번째 줄 : 격자의 크기 n과 반복 횟수 k (1 <= n, k <= 100)
- 두 번째 줄 : n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자 (1 <= 주어지는 숫자 <= 100)
- 마지막 줄 : 시작 위치 r, c (1 <= r, c <= n)

3. 로직 : BFS
- 이동 가능 여부(범위내, 방문X, P값보다 작음) -> 이동(q에 삽입) -> 값이 최댓값보다 크거나 같으면 업데이트
"""

from collections import deque

# 입력 변수
n, k = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]
r, c = map(int, input().split())

# 범위 안에 있는지 여부 판단
def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# 이동 가능 여부 판단
def can_go(y, x):
    if not in_range(y, x):
        return False
    
    if visited[y][x] or grid[y][x] >= P:
        return False
    
    return True

# 도착지 후보 변경 시 위치 업데이트
def update_pos(y, x):
    global max_val, max_pos

    # 후보값보다 크면 후보값과 후보위치 변경
    if grid[y][x] > max_val:
        max_val = grid[y][x]
        max_pos = (y, x)
    # 후보값과 같으면 행, 열 순으로 더 작은 위치로 후보위치 변경
    elif grid[y][x] == max_val:
        if max_pos[0] > y or (max_pos[0] == y and max_pos[1] > x):
            max_pos = (y, x)

# 완전 너비 탐색
def bfs(y, x):
    global visited, max_val, max_pos, P

    # 변수 초기화
    visited = [[False for _ in range(n)] for _ in range(n)]
    max_val, max_pos = 0, (y, x)
    P = grid[y][x]

    visited[y][x] = True
    dys, dxs = [-1, 0, 1, 0], [0, -1, 0, 1]
    q = deque([(y, x)])

    while q:
        
        cy, cx = q.popleft()

        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx

            if can_go(ny, nx):
                visited[ny][nx] = True
                update_pos(ny, nx)
                q.append((ny, nx))


# k번 반복
cur = (r-1, c-1)
for _ in range(k):
    bfs(cur[0], cur[1])
    cur = max_pos

# 정답 출력
print(max_pos[0] + 1, max_pos[1] + 1)