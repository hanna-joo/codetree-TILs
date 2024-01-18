"""
1. 문제 : 움직이는 블록
- INPUT = 각 위치별 블럭의 개수
- WORK = 모든 위치에 놓인 블럭의 개수가 동일해지도록 블럭 옮기기
- OUTPUT = 이동해야 할 최소 블럭의 수 출력

2. 입력 및 제한
- N (1<=N<=10,000)
- N개의 줄에 걸쳐 각 위치별 블럭의 수 (1<=블럭의 수<=10,000)

3. 로직
- 기준 = 동일한 블록 개수 = 총 블록 개수 / N
- 기준보다 많은 곳 -> 적은 곳 (O)
- 기준보다 적은 곳 -> 많은 곳 (X)
- 기준보다 같은 곳 -> 같은 곳 (X)
- 계속 탐색 -> 기준보다 많으면 많은 만큼 빼서 보관 -> 적은 곳 발견하면 주기
"""

N = int(input())
nums = [int(input()) for _ in range(N)]

base = sum(nums) // N
ans = 0
for num in nums:
    ans += (num - base) if num > base else 0

print(ans)