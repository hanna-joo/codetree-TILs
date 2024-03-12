"""
1. 문제
- 연속한 여는 괄호 2개와 연속한 닫는 괄호 2개로 쌍을 이루는 서로 다른 가지수 구하기
- return : 조건을 만족하는 쌍의 서로 다른 가지수 출력 

2. 입력 및 제한
- '('과 ')'로 이루어진 문자열 A (1 <= 문자열 A의 길이 <= 100)

3. solution : 완전탐색 = 
- 처음부터 끝에서 4칸 전까지 탐색
- 현재 위치 i에서 2개 문자열이 '(('인 경우 '))' 탐색 시작
    - i+2부터 끝에서 4칸 전까지 탐색
    - 현재 위치 j에서 2개 문자열이 '))'인 경우 cnt ++1
"""

strings = input().strip()
length = len(strings)

cnt = 0
for i in range(length-3):
    if strings[i:i+2] != '((':
        continue
    for j in range(i+2, length-1):
        if strings[j:j+2] != '))':
            continue
        cnt += 1

print(cnt)