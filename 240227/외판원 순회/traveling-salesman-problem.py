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
"""
import sys

n = int(input())
graph = [[*map(int, input().split())] for _ in range(n)]
visited = [False for _ in range(n)]
min_dist = sys.maxsize


def knock(num, dist, cnt):
    global min_dist
    if cnt == n:
        if num == 0:
            min_dist = min(min_dist, dist)
        return
    
    for i in range(n):
        # 이미 방문한 노드면 스킵
        if visited[i]:
            continue
        # 갈 수 없는 노드면 스킵
        if graph[num][i] == 0:
            continue
        visited[i] = True
        knock(i, dist+graph[num][i], cnt+1)
        visited[i] = False


knock(0, 0, 0)
print(min_dist)