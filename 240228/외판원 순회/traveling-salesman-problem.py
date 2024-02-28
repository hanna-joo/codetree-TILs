"""
1. 문제
- 1번 지점에서 출발 -> 모든 지점 한 번씩 방문 -> 1번 지점으로 돌아옴
- Aij = i번 지점에서 j번 지점으로 이동하는데 드는 비용
- 비용이 0인 경우는 이동할 수 없는 곳
- return : 모든 정점을 방문하고 돌아오는데 필요한 최소 비용의 합

2. 입력 및 제한
- n (2 <= n <= 10)
- n개의 줄에 걸쳐 한 줄에 n개씩의 Aij 정보 주어짐 (0 <= Aij <= 10,000)

3. solution : 백트래킹
- 1번 노드에서 출발 
- 1행에서 0이 아닌 애들 중 하나(a) 선택 + 방문
    -> a행에서 0이 아닌 애들 중 방문 안한 애 선택 + 방문
    -> 모두 방문했으면 종료(단, 종착지가 1번인지 아닌지 파악)
- 재귀 나오면서 방문 기록 취소

4. solution 속도 비교
- 1 : 재귀함수 매개변수 3개 - 1002ms, 28MB
- 2 : 1에서 매개변수 1개 줄임 - 974ms, 28MB
- 3 : 해설 - 447ms, 26MB
"""


import sys

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
picked = []

ans = sys.maxsize


def knock(cur, cnt):
    global ans
    if cnt == n:
        # 마지막 노드가 1번 노드인 경우만 취급
        if cur == 0:
            ans = min(sum(picked), ans)
        return
    
    for i in range(n):
        # 이미 방문한 노드면 스킵
        if visited[i]:
            continue
        # 갈 수 없는 노드면 스킵
        if graph[cur][i] == 0:
            continue

        visited[i] = True
        picked.append(graph[cur][i])

        knock(i, cnt+1)
        
        visited[i] = False
        picked.pop()

knock(0, 0)
print(ans)


"""solution 3
import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n = int(input())
cost = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [False] * n
picked = []

ans = INT_MAX


# 지금까지 방문한 지점의 수를 cnt라 했을 때
# 계속 탐색을 이어서 진행합니다.
def find_min(cnt):
    global ans

    # 모든 지점를 방문했을 때
    # 가능한 지금까지의 비용 합 중
    # 최솟값을 갱신합니다.
    if cnt == n:
        total_cost = 0
        for i in range(n - 1):
            curr_cost = cost[picked[i]][picked[i + 1]]
            # 만약 비용이 0이라면 불가능한 경우이므로 
            # 바로 함수를 빠져나옵니다.
            if curr_cost == 0:
                return
            
            total_cost += curr_cost

        # 최종적으로 1번 지점으로 다시 돌아오는 것 까지 고려해서 계산해줍니다.
        additional_cost = cost[picked[-1]][0]
        if additional_cost == 0:
            return

        # 답을 갱신해줍니다.
        ans = min(ans, total_cost + additional_cost)
        return

    # 방문할 지점을 선택합니다.
    for i in range(n):
        if visited[i]: 
            continue
        
        visited[i] = True
        picked.append(i)

        find_min(cnt + 1)

        visited[i] = False
        picked.pop()

   
# 1번 지점을 시작으로
# 탐색을 진행합니다.
visited[0] = True
picked.append(0)
find_min(1)

print(ans)
"""