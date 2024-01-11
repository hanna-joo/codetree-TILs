"""
1. 문제
- 여러 개의 구슬이 동시에 t번 이동
    - 현재 위치에 있는 숫자보다 더 큰 숫자 칸으로 이동
    - 큰 칸이 여러 개면 우선순위(상하좌우) 높은 칸으로 이동
    - 이동 후 한 칸에 구슬이 2개 이상이면 구슬 모두 사라짐
2. 해결
- 동시에 여러 개의 변화가 일어나는 경우 -> 기존 배열이 아닌 새로운 배열에 변화 저장
- 1. 다음 과정(2-4)을 t초 간 반복한다
- 2. 모든 칸을 탐색한다
    - 2-1. balls에 구슬이 있는지 확인한다
    - 2-2. 구슬이 있으면 상하좌우 돌아가면서 현재 칸보다 큰 값을 찾는다
    - 2-3. 큰 값이 있으면 next_balls 해당 위치에 +1한다
- 3. 모든 탐색이 끝나면 balls를 next_balls로 변경한다
- 4. balls에서 구슬이 2개 이상이면 해당 위치를 0으로 변경한다
- 5. t초 간 2-4 과정을 반복 이후 최종적으로 남은 구슬의 수를 출력한다
"""

n, m, t = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]
balls = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    balls[r-1][c-1] += 1


def search_pos(cy, cx):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    by, bx = cy, cx
    for i in range(4):
        ny, nx = cy+dy[i], cx+dx[i]
        if 0<=ny<n and 0<=nx<n and grid[ny][nx] > grid[by][bx]:
                by, bx = ny, nx
    return by, bx


def move_balls():
    global balls
    # 2. 모든 칸을 탐색한다
    next_balls = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 2-1. balls에 구슬이 있는지 확인한다
            if balls[i][j] == 1:
                ny, nx = search_pos(i, j)
                next_balls[ny][nx] += 1

    # 3. 모든 탐색이 끝나면 balls를 new_balls로 변경한다
    balls = next_balls


def remove_balls():
    # 4. balls에서 구슬이 2개 이상이면 해당 위치를 0으로 변경한다
    for i in range(n):
        for j in range(n):
            if balls[i][j] >= 2:
                balls[i][j] = 0


def count_balls():
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += balls[i][j]
    return cnt


for _ in range(t):
    move_balls()
    remove_balls()

print(count_balls())