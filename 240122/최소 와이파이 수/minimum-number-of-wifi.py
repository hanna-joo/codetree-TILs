# 최소 와이파이 수 (30px)
"""
1. 문제
- 와이파이 설치 -> 설치 위치로부터 특정 거리(m) 이내 모두 사용 가능
- 사람 살지 않아도 정수 위치면 설치 가능
- return : 모든 사람들이 와이파이 사용할 수 있도록 필요한 최소 와이파이 수

2. 입력
- 집 개수(n), 거리(m)
    - 1<=n<=100
    - 1<=m<=100

3. 로직1
- 와이파이를 최대한 오른쪽에 설치하는 것이 좋음
- 사람이 있으면 그 때부터 오른쪽으로 갈 때마다 카운트
- 카운트가 m이 되면 와이파이 1개 추가

4. 로직2
- 사람이 있으면 무조건 현재+m 위치에 와이파이 설치
- 현재+m+m 위치에서 다시 탐색 시작
"""

n, m = map(int, input().split())
houses = [*map(int, input().split())]

ans, pos = 0, 0
while pos < n:
    if houses[pos] == 1:
        ans += 1
        pos += 2 * m + 1
    else:
        pos += 1
print(ans)



# 로직1
# cnt, pos, ready = 0, 0, False
# ans = 0

# while pos < n:
#     if houses[pos] == 1:
#         ready = True
#     if ready:
#         if cnt == m:
#             ans += 1
#             ready, cnt = False, 0
#             pos += max(1, m+1)
#             continue
#         cnt += 1
#     pos += 1

# if ready:
#     ans += 1
# print(ans)