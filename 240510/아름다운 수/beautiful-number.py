"""
<아름다운 수 : BackTracking>
1. 문제
- 아름다운 수
    - 1 이상 4 이하의 숫자로만 이루어짐
    - 해당 숫자만큼 연달아 같은 숫자가 나오는 수 (ex. 1333221)
    - 동일한 숫자에 대해 연달아 같은 숫자의 묶음이 나오는 수 (ex. 111 / 22222222)
    - 단, 222는 아름다운 수가 아님
- return : n자리 아름다운 수의 개수 출력

2. 입력 및 제한
- 첫째 줄 : n (1<=n<=10)

3. 로직
- 자릿수 하나씩 구하기
- 3자릿수 : 111, 122, 221, 333
- 1, 22, 333, 4444
"""

# 입력 변수
n = int(input())

# 글로벌 변수
cur = list()
candidates = list()
ans = 0

# 모든 n자리 수 후보 찾는 함수
def choose(cnt):
    global cur, candidates

    # n자리 모두 다 구했으면 종료
    if cnt == n:
        candidates.append(list(cur))
        return

    for i in range(1, 5):
        cur.append(i)
        choose(cnt+1)
        cur.pop()
    
# 아름다운 수인지 확인하는 함수
def is_beautiful(element):
    prev = [element[0], 1]
    for cur in element[1:]:
        if prev[0] == prev[1]:
            prev = [cur, 1]
        elif cur == prev[0]:
            prev[1] += 1
        else:
            return False
    if prev[0] != prev[1]:
        return False
    return True

choose(0)
ans = 0
for c in candidates:
    if is_beautiful(c):
        ans += 1

print(ans)