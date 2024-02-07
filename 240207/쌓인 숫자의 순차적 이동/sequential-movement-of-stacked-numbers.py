"""
1. 문제
- m번에 걸쳐 숫자들 이동
- 여덟 방향으로 인접한 칸 중 가장 큰 값이 적힌 숫자가 있는 칸으로 이동
    - 단, 이동하는 칸에 숫자 A가 있으면 A 숫자 위에 B가 얹어짐
    - 숫자 A가 이동할 때 그 위에 얹어진 B도 함께 이동함
- 여덟 방향에 아무 숫자도 없다면 움직이지 않음 -> 나중에 None으로 출력
- return : m번의 움직임 이후 상태 출력

2. 입력 및 제한
- 격자의 크기 n, 움직임 횟수 m (2 <= n <= 20, 1 <= m <= 100)
    - n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자 (1 <= k <= n*n)
    - 움직이는 순서대로 m개의 숫자

3. 로직
- 이동할 숫자 찾기 -> 주변 탐색(범위 내) -> 가장 큰 칸으로 이동
"""


def search_target(num):
    for i in range(n):
        for j in range(n):
            for k, x in enumerate(grid[i][j]):
                if x == num:
                    return (i, j, k)


def in_range(y, x):
    return 0 <= y and 0 <= x and y < n and x < n


def search_biggest(cy, cx):
    dys, dxs = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    biggest = -1
    biggest_pos = None

    for i in range(8):
        ny, nx = cy + dys[i], cx + dxs[i]
        if in_range(ny, nx):
            for k in grid[ny][nx]:
                if biggest < k:
                    biggest, biggest_pos = k, (ny, nx)

    return biggest_pos


def move_to_biggest(cy, cx, ck, ny, nx):
    nums = grid[cy][cx][ck:]
    grid[cy][cx] = grid[cy][cx][:ck]
    grid[ny][nx].extend(nums)
    #print(grid[ny][nx])


def simulate(num):
    cy, cx, ck = search_target(num)
    nxt = search_biggest(cy, cx)
    if nxt:
        #print("move", num, "to", nxt)
        ny, nx = nxt
        move_to_biggest(cy, cx, ck, ny, nx)



n, m = map(int, input().split())
grid = [[[i] for i in map(int, input().split())] for _ in range(n)]
targets = [*map(int, input().split())]

for num in targets:
   simulate(num)

for i in range(n):
   for j in range(n):
        if not grid[i][j]:
            print(None)
        else:
            print(*grid[i][j][::-1])