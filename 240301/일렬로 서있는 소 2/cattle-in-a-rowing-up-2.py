"""
1. 문제
- N마리의 소와 소들의 위치, 키가 주어짐
- return : 3마리 소 위치가 i<j<k 면서, 소 키가 Ai<=Aj<=Ak 를 만족하는 서로 다른 쌍의 수 출력

2. 입력 및 제한
- N (1 <= N <= 100)
- N마리의 소의 키 정보 공백을 사이에 두고 주어짐 (1 <= Ai <= 100)

3. solution : 완전탐색
- i<j<k = 3개 뽑을 때 앞에서부터 순서대로 탐색하면 상관 없음
- 3개 뽑기 -> Ai<=Aj<=Ak 확인 -> cnt+1
"""

N = int(input())
heights = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if heights[i] <= heights[j] <= heights[k]:
                cnt += 1

print(cnt)