"""
<계단오르기 : DynamicProgramming>
1. 문제
- 한 번에 2계단 또는 3계단 단위로만 올라갈 수 있음
- n층 높이의 계단에 올라가기 위한 서로 다른 방법의 수
- 단, 1계단이 남은 상황에서는 n층으로 올라갈 수 있는 방법이 없음
- return : n층 높이의 계단에 올라가기 위한 서로 다른 방법의 수%10,007 (불가능하면 0)

2. 입력 및 제한
- 첫째 줄 : n (2<=n<=1,000)

3. 로직
- dp[i] = i층까지 올라가는 방법 = dp[i-2] + dp[i-3]
    - dp[1] = 1층까지 올라가는 방법 = 0
    - dp[2] = 2층까지 올라가는 방법 = 1
    - dp[3] = 3층까지 올라가는 방법 = 1
    - dp[4] = dp[2] + dp[1] = 1
    - dp[5] = dp[3] + dp[2] = 2
"""

# 입력 변수
n = int(input())

# 메모이제이션
dp = [0 for i in range(n + 1)]

# 동적 계획법
for i in range(1, n + 1):
    if i == 1:
        dp[i] = 0
    elif i <= 3:
        dp[i] = 1
    else:
        dp[i] = dp[i-2] + dp[i-3]


print(dp[n] % 10007)