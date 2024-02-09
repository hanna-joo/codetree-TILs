"""
1. 문제
- return : 1부터 n까지의 수를 한 번씩만 사용하여 만들 수 있는 모든 수열 (사전순)

2. 입력 및 제한
- n (1 <= n <= 8)

3. 로직
- 재귀함수, 백트래킹
    - 방문 배열
    - 종료조건 : 3자리 수 모두 생성한 경우
"""

n = int(input())
answer = []
visited = [False for _ in range(n + 1)]

def make_sequence(digit):
    # n자릿 수 모두 만들었으면 멈추기
    if digit == n + 1:
        print(*answer, end = " ")
        print()
        return
    
    for i in range(1, n + 1):
        # 이미 사용한 번호면 넘어가기
        if visited[i]:
            continue
        # 사용 안 한 번호면 방문기록 + 사용
        visited[i] = True
        answer.append(i)
        # 다음 자릿수 선택하러 가기
        make_sequence(digit+1)
        # n자릿 수의 수열 만들고 나왔기 때문에 초기화하고 종료
        answer.pop()
        visited[i] = False


make_sequence(1)