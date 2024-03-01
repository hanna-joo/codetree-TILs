"""
1. 문제
- return : 주어진 문자열에서 여닫는 괄호 쌍이 될 수 있는 가지수 출력

2. 입력 및 제한
- 문자 '(', ')'로만 이루어진 문자열 A (1 <= len(A) <= 100)

3. solution : 완전탐색
- 처음부터 탐색 시작
- '('를 만나면 다음 과정 반복
    - 이후부터 ')'를 만날 때마다 cnt+1
"""

string = input().strip()
cnt = 0

for i in range(len(string)):
    if string[i] == '(':
        for j in range(i+1, len(string)):
            if string[j] == ')':
                cnt += 1

print(cnt)