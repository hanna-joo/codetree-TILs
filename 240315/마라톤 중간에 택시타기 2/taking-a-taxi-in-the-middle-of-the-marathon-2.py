"""
1. 문제
- 마라톤 코스 N개 체크포인트를 모두 번호 순서대로 방문 후 N번에서 끝남
- 개발자는 1번과 N번을 제외한 1개의 체크포인트를 몰래 건너뛰고자 함
- 맨해튼 거리 = |x1 - x2| + |y1 - y2|
- return : 개발자가 마라톤 완주를 위한 최소 거리(맨해튼 거리) 출력

2. 입력 및 제한
- 체크포인트 N (3<=N<=100)
- N개의 줄에 걸쳐 한 줄에 하나씩 각 번호에 해당하는 지점의 위치(x, y) 공백을 두고 주어짐 (-1,000<=x, y<=1,000)

3. solution : 완전탐색 = 
- (i번 체크포인트 스킵하면서 마라톤 완주) * N번 반복
"""

import sys

INT_MAX = sys.maxsize

N = int(input())
points = [[*map(int, input().split())] for _ in range(N)]

min_dist = INT_MAX

for skip in range(1, N-1):
    dist = 0
    cx, cy = points[0][0], points[0][1]
    cur = 1
    for nx, ny in points[1:]:
        if skip != cur:
            dist += abs(cx - nx) + abs(cy - ny)
            cx, cy = nx, ny
        cur += 1
    min_dist = min(dist, min_dist)

    

print(min_dist)