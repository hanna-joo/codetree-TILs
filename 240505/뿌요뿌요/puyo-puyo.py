"""
<뿌요뿌요 : DFS>
1. 문제
- 상하좌우로 인접한 칸끼리 같은 숫자로 이루어져 있는 여러 칸 = 하나의 블럭
- 4칸 이상으로 구성된 블럭은 터지게 됨
- return : 초기 상태에서 터지는 블럭 수와 최대 블럭의 크기

2. 입력 및 제한
- 첫 번째 줄 : 격자의 크기 n (1 <= n <= 100)
- 두 번째 줄 : n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자 (1 <= 주어지는 숫자 <= 100)

3. 로직 : DFS
- 각 칸마다 블럭 탐색
    - 상하좌우로 이동 가능 여부(범위내, 방문X, 같은 숫자)
    - 다음 칸으로 이동 후 방문 기록
    - 칸 이동 시마다 칸 개수 세기 block+1
    - 블럭 탐색 종료했는데 칸 개수가 4칸 이상이면 boom+1
- 시간복잡도 : O(N^2) - 중복 탐색 X
- 공간복잡도 : O(N^2)
"""

# 입력 변수
n = int(input())
grid = [[*map(int, input().split())] for _ in range(n)]

# 글로벌 변수
boom_cnt = 0             # 터지게 되는 블럭 개수
block_size = 0           # 블럭의 칸 개수
max_block_size = 0       # 최대 블럭의 칸 개수
visited = [[False for _ in range(n)] for _ in range(n)]


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def can_move(y, x, num):
    if not in_range(y, x):
        return False
    
    if visited[y][x] or grid[y][x] != num:
        return False
    
    return True


def dfs(y, x):
    global block_size

    visited[y][x] = True
    block_size += 1
    
    dys, dxs = [-1, 0, 1, 0], [0, -1, 0, 1]

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx

        if can_move(ny, nx, grid[y][x]):
            dfs(ny, nx)


for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        # 새로운 블럭 탐색을 위해 칸 개수 초기화
        block_size = 0

        # 블럭 칸 개수 탐색
        dfs(i, j)

        # 블럭 칸 최대 개수 업데이트 
        if block_size > max_block_size:
            max_block_size = block_size

        # 블럭 크기가 4개 이상이면 터짐
        if block_size >= 4:
            boom_cnt += 1

print(boom_cnt, max_block_size)