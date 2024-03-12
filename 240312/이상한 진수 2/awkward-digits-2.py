"""
1. 문제
- 정수 N을 2진법으로 나타내고 정확히 한 숫자만을 바꾼 숫자 a가 주어졌을 때 가능한 숫자 N
- return : 가능한 숫자 N 중 최댓값 출력

2. 입력 및 제한
- a는 모두 숫자 0과 1로 이루어져 있음(맨 앞은 0이 아님)
- a (0 <= a의 자릿 수 <= 10)

3. solution : 완전탐색 = O(N^2)
- 1000 -> 1111 : 0이 1개라도 있는 경우 -> 맨 앞에 있는 0을 1로 변경
- 1111 -> 1110 : 0이 1개도 없는 경우 -> 끝 자리만 0으로 변경
"""

two = input().strip()

for i, x in enumerate(two):
    if x == '0':
        ans = two[:i] + '1' + two[i+1:]
        break
    if i == len(two) - 1 and x == '1':
        ans = two[:i] + '0'

print(int('0b' + ans, 2))