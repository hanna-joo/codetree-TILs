"""
1. 문제
- return : n개의 집 중 한 곳에 전부 모일 때 사람들의 이동 거리 합 중 최솟값 출력

2. 입력 및 제한
- n (1 <= n <= 100)
- 각 지점에 살고 있는 사람 수에 해당하는 n개의 숫자 주어짐 (1 <= Ai <= 100)

3. solution : 완전탐색
- 0번 집에 모일 때 = (0번 사람 수 * 0) + (1번 사람 수 * 1) + ... + (4번 사람 수 * 4)
- 1번 집에 모일 때 = (0번 사람 수 * 1) + (1번 사람 수 * 0) + ... + (4번 사람 수 * 3)
"""

import sys

INT_MAX = sys.maxsize

n = int(input())
houses = list(map(int, input().split()))

ans = INT_MAX


def calculate_distance(num):
    dist = 0
    for i in range(n):
        dist += houses[i] * abs(num - i)
    return dist


def simulate():
    global ans
    for i in range(n):
        ans = min(ans, calculate_distance(i))


simulate()
print(ans)