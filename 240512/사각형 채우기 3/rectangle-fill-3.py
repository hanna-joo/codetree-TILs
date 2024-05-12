"""
[DP : subproblem을 그대로 합치면 되는 DP]
1. 문제 : 사각형 채우기 3
- 2 * n 크기의 사각형을 1 * 2, 2 * 1, 1 * 1 크기의 사각형들로 채우는 방법의 수
    - ex. n = 2 일 때 7가지
- return : 2 * n 크기의 사각형 채우는 방법의 수 % 1,000,000,007

2. 입력 및 제한
- 첫째 줄 : n (1 <= n <= 1,000)

3. 로직
- 사각형 추가하는 방법
    - 1칸 추가하는 방법 : |, : -> 총 2가지
    - 2칸 추가하는 방법 : = 외 2가지 -> 총 3가지
- dp[i] = dp[i-1] * 2 + dp[i-2] * 3
    - dp[1] = |, : -> 2가지
    - dp[2] = ||, :|, |:, ::, = 외 2가지 -> 7가지
"""

MAX_N = 1000
MOD = 1000000007

# 입력 변수
n = int(input())

# 메모이제이션
dp = [0 for _ in range(MAX_N + 1)]

# 초깃값 설정
dp[1] = 2
dp[2] = 7

# 동적 프로그래밍
for i in range(3, n + 1):
    dp[i] = dp[i-1] * 2 + dp[i-2] * 3


print(dp[n] % MOD)