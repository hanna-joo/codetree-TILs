"""
1. 문제
- return : 1부터 n까지의 수를 한 번씩만 사용하여 만들 수 있는 모든 수열 (사전순 반대)

2. 입력 및 제한
- n (1 <= n <= 8)

3. 로직
- 재귀함수, 백트래킹
    - 방문 배열
    - 종료조건 : 3자리 수 모두 생성한 경우
"""

n = int(input())
visited = [False for _ in range(n+1)]
answer = []

def make_sequence(digit):
    if digit == n + 1:
        print(*answer, end = " ")
        print()
        return
    
    for i in range(n, 0, -1):
        if visited[i]:
            continue
        visited[i] = True
        answer.append(i)

        make_sequence(digit+1)

        visited[i] = False
        answer.pop()


make_sequence(1)