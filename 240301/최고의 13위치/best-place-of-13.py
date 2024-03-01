"""
1. 문제
- return : N*N 격자 내에서 1*3 격자 범위 내에 있는 동전 개수 중 최댓값 출력
2. 입력 및 제한
- N (3 <= n <= 20)
- N개의 줄에 걸쳐 격자 정보(0과 1로 이루어진 N개의 숫자) 제공

3. solution : 완전탐색 = O(N^2)
- 첫 번째 행부터 탐색
    - 각 행의 1열부터 N-2열까지 3칸씩 탐색
    - 최댓값 업데이트
"""

import sys

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N-2):
        cnt = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        ans = max(ans, cnt)

print(ans)