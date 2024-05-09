"""
1. 문제
- 1 이상 K 이하의 숫자를 하나 고르는 행위 N번 반복하여 나올 수 있는 모든 서로 다른 순서쌍
- return : 1~K로 이루어진 N개의 수인 쌍 모두 출력

2. 입력 및 제한
- 첫째 줄 : K와 N 공백
- 1 <= K <= 4
- 1 <= N <= 8
"""

# 입력 변수
K, N = map(int, input().split())

# 글로벌 변수
ans = []

def print_answer(ans):
    for i in ans:
        print(i, end=" ")
    print()


def choose(num):
    if num == N + 1:
        print_answer(ans)
        return

    for i in range(1, K+1):
        ans.append(i)
        choose(num+1)
        ans.pop()


choose(1)