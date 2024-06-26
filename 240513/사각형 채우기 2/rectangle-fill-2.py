"""
[DP : subproblem을 그대로 합치면 되는 DP]
1. 문제 : 사각형 채우기 2
- 2 * n 크기의 사각형을 1 * 2, 2 * 1, 2 * 2 크기의 사각형들로 채우는 방법의 수
    - ex. n = 2 일 때 3가지
- return : 2 * n 크기의 사각형 채우는 방법의 수 % 10,007

2. 입력 및 제한
- 첫째 줄 : n (1 <= n <= 1,000)

3. 로직
- 사각형 추가하는 방법
    - 1칸으로만 추가할 수 있는 고유 방법 : | -> 총 1가지
    - 2칸으로만 추가할 수 있는 고유 방법 : = ㅁ -> 총 3가지
- dp[i] = dp[i-1] + 2 * dp[i-2]
"""

MAX_N = 1000
MOD = 10007

# 입력 변수
n = int(input())

# 메모이제이션
dp = [0 for _ in range(MAX_N)]
dp[1] = 1
dp[2] = 3

# 동적 계획법
for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2] * 2

# 정답 출력
print(dp[n] % MOD)