"""
1. 문제
- 명예의 전당에 올라간 사람의 조합이 변경된 횟수 
- 동점 시 두 명 다 올라감

2. 로직
- 점수 변경 -> 1등 선별 -> 1등 변동 여부 확인 -> 변동 시 ans+=1
    - A = B, A > B, A < B
"""

change_cnt = int(input())
scores = {'A': 0, 'B': 0}
winners = ['A', 'B']
answer = 0
for _ in range(change_cnt):
    player, change = input().split()
    scores[player] += int(change)
    if scores['A'] == scores['B']:
        tmp = ['A', 'B']
    elif scores['A'] > scores['B']:
        tmp = ['A']
    else:
        tmp = ['B']
    if winners != tmp:
        winners = tmp
        answer += 1
print(answer)