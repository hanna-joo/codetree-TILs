"""
1. 문제
- 정수 N을 2진법으로 나타내고 정확히 한 숫자만을 바꾼 숫자 a가 주어졌을 때 가능한 숫자 N
- return : 가능한 숫자 N 중 최댓값 출력

2. 입력 및 제한
- a는 모두 숫자 0과 1로 이루어져 있음(맨 앞은 0이 아님)
- a (0 <= a의 자릿 수 <= 10)

3. solution : 알고리즘 = O(N)
- 1000 -> 1111 : 0이 1개라도 있는 경우 -> 맨 앞에 있는 0을 1로 변경
- 1111 -> 1110 : 0이 1개도 없는 경우 -> 끝 자리만 0으로 변경

4. solution : 완전탐색

"""

import sys

INT_MIN = -sys.maxsize

binary = list(map(int, list(input())))
length = len(binary)

ans = INT_MIN
for i in range(length):
    # i번째 자릿수 변경
    binary[i] = 1 - binary[i]
    # 십진수로 변경
    num = 0
    for j in range(length):
        num = num * 2 + binary[j]
    # 최댓값과 비교
    ans = max(ans, num)
    # i번째 자릿수 원래대로 원상복귀
    binary[i] = 1 - binary[i]

print(ans)

"""solution : 알고리즘
binary = input().strip()

for i, x in enumerate(binary):
    if x == '0':
        ans = binary[:i] + '1' + binary[i+1:]
        break
    if i == len(binary) - 1 and x == '1':
        ans = binary[:i] + '0'

print(int('0b' + ans, 2))
"""