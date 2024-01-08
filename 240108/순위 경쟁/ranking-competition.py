# 명예의 전당에 올라간 사람의 조합의 변경 횟수

# 해결1 : 점수 저장 > 정렬 > 비교
# scores = {'A': 0, 'B': 0, 'C': 0}
# fame = ['A', 'B', 'C']
# ans = 0
# for _ in range(int(input())):
#     c, s = input().split()
#     scores[c] += int(s)
#     new_fame = [k for k, v in scores.items() if v >= max(scores.values())]
#     if new_fame != fame:
#         fame = new_fame
#         ans += 1
# print(ans)

# 해결2 : 7가지 상황 정의 및 코드 부여 > 비교
n = int(input())
changes = [input().split() for _ in range(n)]
score_a, score_b, score_c = 0, 0, 0

def get_status(score1, score2, score3):
    return_val = 0
    max_val = max([score1, score2, score3])

    if max_val == score1:
        return_val += 1

    if max_val == score2:
        return_val += 2

    if max_val == score3:
        return_val += 4

    return return_val

ans = 0
for name, value in changes:
    value = int(value)
    if name == 'A':
        if get_status(score_a, score_b, score_c) != get_status(score_a + value, score_b, score_c):
            ans += 1
        score_a = score_a + value
    elif name == 'B':
        if get_status(score_a, score_b, score_c) != get_status(score_a, score_b + value, score_c):
            ans += 1
        score_b = score_b + value
    else:
        if get_status(score_a, score_b, score_c) != get_status(score_a, score_b, score_c + value):
            ans += 1
        score_c = score_c + value

print(ans)