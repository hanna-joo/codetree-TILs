# 명예의 전당에 올라간 사람의 조합의 변경 횟수
scores = {'A': 0, 'B': 0, 'C': 0}
fame = ['A', 'B', 'C']
ans = 0
for _ in range(int(input())):
    c, s = input().split()
    scores[c] += int(s)
    new_fame = [k for k, v in scores.items() if v >= max(scores.values())]
    if new_fame != fame:
        fame = new_fame
        ans += 1
print(ans)