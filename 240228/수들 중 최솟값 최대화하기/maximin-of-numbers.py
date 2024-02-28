"""
1. 문제
- 총 n개의 칸을 칠하는데, 행과 열이 겹치지 않아야 함
- 칠한 n개의 칸 중 최솟값의 경우 중 최대인 경우
- return : 색칠된 칸에 적힌 수들의 최솟값이 될 수 있는 값들 중 최대 출력

2. 입력 및 제한
- n (1 <= n <= 10)
- n개의 줄에 걸쳐 한 줄에 n개씩의 정수가 주어짐 (0 <= 주어진 정수 <= 10,000)

3. solution : 백트래킹
- 1행 칸 선택
    > 1-n번 열 중 선택
    > 선택한 열의 방문기록
    > 2행 칸 선택(재귀)...
    > n행 칸까지 선택했으면 종료하고 return
    > 나오면 방문기록 복구
"""

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
picked = []
visited = [False for _ in range(n)]
ans = 0

def color(num):
    global ans

    if num == n:
        ans = max(ans, min(picked))
        return
    
    for i in range(n):
        if visited[i]:
            continue
        
        picked.append(grid[num][i])
        visited[i] = True
        
        color(num+1)
        
        visited[i] = False
        picked.pop()

color(0)
print(ans)