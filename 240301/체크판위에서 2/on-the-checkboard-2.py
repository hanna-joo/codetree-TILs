"""
1. 문제
- R * C 크기의 직사각형의 칸은 W, B로 이루어짐
- 왼쪽 상단(1, 1)에서 우측 하단(R, C)으로 이동 성공하는 경우의 수
    - 현재 위치에 적힌 색과 점프한 곳의 색이 달라야 함
    - 현재 위치에서 최소 한칸 이상 아래이면서 오른쪽에 있는 위치여야 함(+1, +1)
    - 시작과 도착 지점 제외하고 정확히 2곳만 들러야 함
- return : 첫 번재 줄에 룰을 만족하면서 이동에 성공할 수 있는 경우의 수 출력

2. 입력 및 제한
- 직사각형의 세로변 R, 가로변 C (5 <= R, C <= 15)
- R * C 크기의 직사각형 W, B로 주어짐

3. solution : 완전탐색
- 처음에 (1, 1)와 (R, C)가 다른지 확인
- 첫번째 점프 : (1, 1) = W이라고 가정
- 두번째 점프 : 2행부터 C-2행까지 탐색 -> B인 칸 찾으면 세번째 칸 찾기(이 때 j행)
- 세번째 칸 : j행부터 C-1행까지 탐색 -> W인 칸 찾으면 cnt+1
- 칸 없으면 다음 탐색으로 넘어가기
"""
"""
R, C = map(int, input().split())
arr = [input().split() for _ in range(R)]

if arr[0][0] == arr[R-1][C-1]:
    print(0)
    exit()

cnt = 0
for i in range(1, R-2):
    for j in range(1, C-2):
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                if arr[i][j] != arr[0][0] and arr[k][l] != arr[i][j]:
                    cnt += 1


print(cnt)
"""

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    input().split()
    for _ in range(n)
]

# 이동 시에 행과 열이 전부 증가하도록
# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i + 1, n - 1):
            for l in range(j + 1, m - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[n - 1][m - 1]:
                    cnt += 1
                        
print(cnt)