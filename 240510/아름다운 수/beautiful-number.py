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
- 모든 자릿수 구하기 -> 아름다운 수인지 판별하기
    - 3자릿수 : 111, 122, 221, 333
"""

# 입력 변수
n = int(input())

# 글로벌 변수
seq = []
ans = 0

# 아름다운 수인지 확인하는 함수
def is_beautiful():
    prev = [seq[0], 1]
    for cur in seq[1:]:
        # 이전 값이 부분 아름다운 수면 값 초기화
        if prev[0] == prev[1]:
            prev = [cur, 1]
        # 이전 값과 현재 값이 같으면 이전 값 카운트+1
        elif cur == prev[0]:
            prev[1] += 1
        # 이전 값이 부분 아름다운 수도 아니고, 이전 값과 현재 값이 다르면 아름다운 수가 아님
        else:
            return False

    if prev[0] != prev[1]:
        return False

    return True

# 모든 n자리 수 후보 찾는 함수
def count_beautiful_seq(cnt):
    global seq, ans

    # n자리 모두 다 구했으면 종료
    if cnt == n:
        if is_beautiful():
            ans += 1
        return

    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt+1)
        seq.pop()
    


count_beautiful_seq(0)

print(ans)