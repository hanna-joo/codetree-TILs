"""
1. 문제
- 정확히 n개의 칸에 색칠을 하여 각 행과 열에 1개의 칸만 색칠
- return : 색칠한 칸에 적힌 수들의 합 최댓값 출력

2. 입력 및 제한
- n (1 <= n <= 10)
- n개의 줄에 걸쳐 한 줄에 n개씩의 정수가 공백을 두고 주어짐 (1 <= 주어지는 정수 <= 10,000)

3. 로직
- 색칠할 칸 정하고 색칠하기
    - n개 다 색칠했으면 max값 비교 후 종료
    - 행 고르기 : 0~n-1 탐색 -> 이미 선택한 행이면 넘어가기 -> 선택 후 방문 등록
    - 열 고르기 : 0~n-1 탐색 -> 이미 선택한 열이면 넘어가기 -> 선택 후 방문 등록
    - 현재 칸 색칠하기
    - 다음 칸 색칠하러 가기
    - 방문 등록과 칸 합 초기화
"""

import sys

n = int(input())
grid = [[*map(int, input().split())] for _ in range(n)]
max_ans = -sys.maxsize
ans = 0
visited_y = [False for _ in range(n)]
visited_x = [False for _ in range(n)]


def color(num):
    global max_ans, ans
    # n개의 칸 색칠했으면 종료
    if num == n:
        print('colored')
        if ans > max_ans:
            max_ans = ans
        return  

    # 행 고르기
    for y in range(n):
        if visited_y[y]:
            continue
        visited_y[y] = True
        
        # 열 고르기    
        for x in range(n):
            if visited_x[x]:
                continue
            visited_x[x] = True
            
            #print(y, x)
            ans += grid[y][x]
            color(num+1)
            ans -= grid[y][x]

            visited_x[x] = False
        
        visited_y[y] = False
    
    

# 0칸에서 시작
color(0)
print(max_ans)